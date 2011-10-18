from django import forms
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationFormUniqueEmail

from common.utils import update_sorted_dict_order

class DCRegistrationForm(RegistrationFormUniqueEmail):
    """
    Why not let people specify a first and last name
    """

    def __init__(self, *args, **kwargs):
        super(DCRegistrationForm, self).__init__(*args, **kwargs)

        # override super -- incorrect error message
        self.fields['username'].error_messages['invalid'] = (
                'This value must contain only letters, '
                'numbers, _, ., @, +, or -.')

        # XXX Default is to display fields in the order they were defined,
        # which is a pain for inheritance.
        update_sorted_dict_order(self.fields,
            ['firstname', 'lastname', 'username',
                    'email', 'password1', 'password2'])

    firstname = forms.RegexField(regex=r'^\w*$',
                                max_length=30,
                                widget=forms.TextInput(),
                                required=False,
                                label=_(u'first name'))
    lastname = forms.RegexField(regex=r'^\w*$',
                                max_length=30,
                                widget=forms.TextInput(),
                                required=False,
                                label=_(u'last name'))

    def save(self, profile_callback=None):
        """
        Do a regular save, and then put the name in the DB too
        """
        new_user = super(DCRegistrationForm, self).save(profile_callback)
        if new_user:
            new_user.first_name = self.cleaned_data['firstname']
            new_user.last_name = self.cleaned_data['lastname']
            new_user.save()

        return new_user
