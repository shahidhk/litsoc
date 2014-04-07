from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'events.views.event_main', name='event_main'),
    url(r'^create_event$', 'events.views.create_event', name='create_event'),
    url(r'^add_venue$', 'events.views.add_venue', name='add_venue'),
    url(r'^edit_event/(?P<event_id>\d+)/$', 'events.views.edit_event', name='edit_event'),
    url(r'^delete_event/(?P<event_id>\d+)/$', 'events.views.delete_event', name='delete_event'),
)