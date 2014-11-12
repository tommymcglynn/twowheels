from django.conf.urls import patterns, url, include
from rest_framework import routers
from web import views
from web import api


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'bikes', api.BikeViewSet)

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls)),
)
