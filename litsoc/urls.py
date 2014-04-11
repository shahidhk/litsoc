from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', RedirectView.as_view(url='home/')),
    url(r'^$', include('home.urls')),
    url(r'^clubs/', include('clubs.urls')),
    url(r'^gallery/', include('gallery.urls')),
    url(r'^points/', include('points.urls')),
    url(r'^updates/', include('updates.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^userprofile/', include('userprofile.urls')),

    url(r'^summernote/', include('django_summernote.urls')),

    url(r'^ext/', include('django_select2.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),


)
