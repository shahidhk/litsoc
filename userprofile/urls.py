from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login$', 'userprofile.views.login', name='login'),
    url(r'^logout$', 'userprofile.views.logout', name='logout'),
    url(r'^add_user$', 'userprofile.views.add_user', name='add_user'),
    url(r'^edit_profile$', 'userprofile.views.edit_profile', name='edit_profile'),
    url(r'^change_password$', 'userprofile.views.change_password', name='change_password'),
)