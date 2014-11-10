from django.conf.urls import patterns, url
from web import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^bikes$', views.bikes, name='bikes'),
    url(r'^bikes/(?P<bike_id>\d+)', views.bike_detail, name='bike_detail'),
)
