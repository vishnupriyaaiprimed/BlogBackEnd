from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.authtoken.views import ObtainAuthToken
from . import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'usersbyusername', views.UserViewSetByUsername)
router.register(r'profiles', views.ProfileViewSet)

urlpatterns=[
    url(r'^', include(router.urls)),
    url(r'^auth/',ObtainAuthToken.as_view())
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)