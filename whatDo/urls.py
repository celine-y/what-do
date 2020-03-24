from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from .views import ActivityViewSet, EffortViewSet
from allauth.account.views import confirm_email

router = DefaultRouter()
router.register('activity', ActivityViewSet)
router.register('effort', EffortViewSet)

urlpatterns = [
    re_path('', include(router.urls)),
    path('user/', include('accounts.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('account/', include('allauth.urls')),
]
