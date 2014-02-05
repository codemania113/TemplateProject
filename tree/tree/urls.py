import settings


from django.conf.urls import patterns, include, url
from django.contrib import admin
from tree.project_views import load


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'(?P<addr>[^\f]+)/$', load, {}),
    )




    
    
