from django.conf.urls.defaults import patterns, url
from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


view = TemplateView.as_view(template_name='dummy.html')

urlpatterns = patterns('',
    url(_(r'^register/$'), view, name='register'),
)
