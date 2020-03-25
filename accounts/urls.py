from django.urls import path, include, re_path
from .views import UserViewSet, FollowerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('user', UserViewSet)
# router.register('follower', FollowerViewSet)


urlpatterns = [
    re_path('', include(router.urls))
]
