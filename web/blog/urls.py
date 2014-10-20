from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)

urlpatterns += patterns('apps.home.views',
    url(r'^index$', 'index'),
    url(r'^/$', 'index'),
    url(r'^blog/(?P<blog_id>[0-9]+)$', 'blog'),
    url(r'^info$', 'info'),
)