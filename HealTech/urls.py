from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns

from .views import index
from .views import contact_us, make_an_appointment

urlpatterns = [
    url(r'^$', index, name='main_page'),
    url(r'^contact/', contact_us, name='contact_us'),
    url(r'^make_an_appointment/(?P<doc_id>\d)/$', make_an_appointment, name='make_appointment'),
]