from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'clubs.views.club_main', name='club_main'),
    url(r'^create_club$', 'clubs.views.create_club', name='create_club'),
    url(r'^edit_club/(?P<club_id>\d+)/$', 'clubs.views.edit_club', name='edit_club'),
    url(r'^delete_club/(?P<club_id>\d+)/$', 'clubs.views.delete_club', name='delete_club'),
    url(r'^musicroom1/$', 'clubs.views.musicroom1', name='musicroom1'),
    url(r'^musicroom2/$', 'clubs.views.musicroom2', name='musicroom2'),
    url(r'^approval/$', 'clubs.views.approval', name='approval'),
    url(r'^cancel_musicroom_approval/(?P<slot_id>\d+)/$', 'clubs.views.cancel_musicroom_approval', name='cancel_musicroom_approval'),
)