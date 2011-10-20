from django.conf import settings
from django.utils.safestring import mark_safe

def analytics(request):
    return {'ANALYTICS': mark_safe(
"""<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', '%(key)s']);
  _gaq.push(['_setDomainName', 'none']);
  _gaq.push(['_anonymizeIp']);
  _gaq.push(['_setVisitorCookieTimeout', 21*24*60*60*1000 ]); // 3 weeks in ms
  _gaq.push(['_trackPageLoadTime']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>""" % {'key': settings.ANALYTICS_KEY})}
