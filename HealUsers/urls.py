from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import login_page
from .views import profile, log_out, fill_profile, doc_profile
from .views import register_user

urlpatterns = [
    # url(r'^login/', login_page, name='login'),
    # url(r'^logout/', log_out, name='logout'),

    url(r'^login/$',
        login_page,
        name='login'),
    url(r'^logout/$',
        auth_views.logout,
        {'next_page': 'index'},
        name='logout'),

    url(r'^register/', register_user, name='register'),
    url(r'^profile/', profile, name='profile'),
    url(r'^profile/fill_profile', fill_profile, name='fill_profile'),
    url(r'^doctor/(?P<doc_id>\d)/$', doc_profile, name='doctor_profile')
]
