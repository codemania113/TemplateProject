import django
from django.conf.urls import patterns
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.http import HttpResponseRedirect

import settings

import tree
from tree.project_views import load


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', lambda r : HttpResponseRedirect('stories-and-literature/')),
    url(r'^$', load, {'addr': 'stories-and-literature'}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'(?P<addr>[^\f]+)/$', load, {}),
    )




    
    
