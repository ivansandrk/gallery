from django.conf.urls.defaults import patterns, url
from django.views.generic.simple import redirect_to


urlpatterns = patterns('gallery.views',
    url(r'^$', redirect_to, {'url': 'list/'}),
    url(r'^list/$', 'list', name='list'),
    url(r'^image/(?P<image_id>\d+)/$', 'image', name='image'),
)
