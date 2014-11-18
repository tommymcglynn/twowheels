from django.conf.urls import patterns, url, include
from rest_framework import routers
from django.contrib import admin
from web import views
from web import api


admin.autodiscover()

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'bikes', api.BikeViewSet)
router.register(r'styles', api.BikeStyleViewSet)
router.register(r'models', api.BikeModelViewSet)
router.register(r'parts', api.BikePartViewSet)

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^api/', include(router.urls), name='api-root'),
)
