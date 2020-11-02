# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve
from solid_i18n.urls import solid_i18n_patterns

from django.conf.urls.static import static

admin.autodiscover()

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
    #url(r'^catalog/', include('catalog.urls')),
    url(r'^', include('products.urls')),
    url(r'^', include('orders.urls')),
    #url(r'^ru/', include('formsend.urls')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^goods/', include('goods.urls')),
]



urlpatterns += solid_i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),  # NOQA
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
        url(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ] + staticfiles_urlpatterns() + urlpatterns

#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOM)
#+ static(settings.MEDIA_URL, document_root=settings.STATIC_ROOM)