import settings


from django.conf.urls import patterns, include, url
from django.contrib import admin
from tree.project_views import load


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^stories-and-literature/$', load, {'addr': 'stories-and-literature'}),
    url(r'stories-and-literature/([a-zA-Z0-9_.-]+/)*(?P<addr>[a-zA-Z0-9_.-]+)/$', load, {}),
)
