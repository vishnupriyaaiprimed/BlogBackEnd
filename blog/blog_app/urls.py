from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from . import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'usersbyusername', views.UserViewSetByUsername)

urlpatterns=[
    url(r'^', include(router.urls)),
    url(r'^auth/',ObtainAuthToken.as_view())
]