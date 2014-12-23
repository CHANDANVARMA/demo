from django.conf.urls import patterns, include, url
from django.contrib import admin
from view import login,logout,spice,view_tracker#,GetSearchAndroid

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^spice/$', spice, name='spice'),
    url(r'^view_tracker/$', view_tracker, name='view_tracker'),
    #url(r'^GetSearchAndroid/$', GetSearchAndroid, name='GetSearchAndroid'),
)
