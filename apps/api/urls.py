from rest_framework import routers

from django.conf.urls import url, include

from apps.api import views


router = routers.DefaultRouter()
router.register(r'campaigns', views.CampaignViewSet)
router.register(r'channels', views.ChannelViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
