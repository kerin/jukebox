# -*- coding: UTF-8 -*-

from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns("",
    url(r"^admin/", include(admin.site.urls)),
    url(r"^admin/doc/", include("django.contrib.admindocs.urls")),

    url(r'', include('jukebox.jukebox_web.urls')),
    url(r'', include('jukebox.jukebox_core.urls')),
    url(r'', include('social_auth.urls')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
