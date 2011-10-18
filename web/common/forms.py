from django import forms
from django.utils.translation import ugettext_lazy as _
from registration.forms import RegistrationForm

# I put this on all required fields, because it's easier to pick up
# on them with CSS or JavaScript if they have a class of "required"
# in the HTML. Your mileage may vary. If/when Django ticket #3515
# lands in trunk, this will no longer be necessary.
attrs_dict = { 'class': 'required' }


class DCRegistrationForm(RegistrationForm):
    """
    Why not let people specify a first and last name
    """
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
