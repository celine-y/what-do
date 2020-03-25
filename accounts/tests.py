from django.test import TestCase
from django.urls import reverse
from rest_framework.test import (APITestCase,
    APIClient)

from rest_framework.exceptions import PermissionDenied

from rest_framework.views import status
from whatDo.models import Effort, Activity
from whatDo.serializers import EffortSerializer
from accounts.models import User
from accounts.serializers import UserSerializer, UserDetailSerializer

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(email="", password=""):
        return User.objects.create(email=email, password=password)

    @staticmethod
    def create_activity(name, description, user):
        return Activity.objects.create(
            name=name,
            description=description,
            created_by=user)

    @staticmethod
    def create_effort(user, activity, caption="", media=None):
        return Effort.objects.create(
            created_by=user,
            activity=activity,
            media=media,
            caption=caption
        )

    def setUp(self):
        self.user = self.create_user("user1@example.com", "p@ssw0rd")
        self.user2 = self.create_user("user2@example.com", "p@ssw0rd")
        self.activity = self.create_activity("dance", "create a new dance", self.user2)
        self.eff1 = self.create_effort(self.user, self.activity)
        self.eff2 = self.create_effort(self.user, self.activity)

class ViewUserTest(BaseViewTest):

    def test_user_can_view_own_effort(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('user-detail',
            kwargs={'pk': self.user.pk}))

        serialized = UserDetailSerializer(self.user)

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_can_view_other_effort(self):
        self.client.force_login(self.user2)

        response = self.client.get(reverse('user-detail',
            kwargs={'pk': self.user.pk}))

        serialized = UserDetailSerializer(self.user)

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
