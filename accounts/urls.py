from django.urls import path, include
from .views import ListUserView


urlpatterns = [
    path('', ListUserView.as_view(), name="user-all")
]
