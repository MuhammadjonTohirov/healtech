from django.conf.urls import url

from .views import table_department, create_comment

urlpatterns = [
    url(r'^$', table_department, name='forum'),
    url(r'comment/(?P<id>\d+)/$', create_comment, name='comment'),
]
