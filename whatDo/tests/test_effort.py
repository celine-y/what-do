from django.test import TestCase
from django.urls import reverse
from rest_framework.test import (APITestCase,
    APIClient)

from rest_framework.exceptions import PermissionDenied

from rest_framework.views import status
from whatDo.models import Effort, Activity
from whatDo.serializers import EffortSerializer
from accounts.models import User

# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_activity(name, description, user):
        return Activity.objects.create(
            name=name,
            description=description,
            created_by=user)

    @staticmethod
    def create_effort(user, activity, caption="", media=None):
        print(user)
        return Effort.objects.create(
            created_by=user,
            activity=activity,
            media=media,
            caption=caption
        )

    def setUp(self):
        self.user = User.objects.create_user("user1@example.com", "p@ssw0rd")
        self.user2 = User.objects.create_user("user2@example.com", "p@ssw0rd")
        self.activity = self.create_activity("dance", "create a new dance", self.user2)
        self.eff1 = self.create_effort(self.user, self.activity)

class UpdateEffortTest(BaseViewTest):

    def test_not_creator_update_effort(self):
        self.client.force_login(self.user2)

        response = self.client.put(
            reverse('effort-detail', kwargs={'pk': self.eff1.pk}),
            {
            'caption': 'new caption',
            'activity': self.activity.pk
            },
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_creator_update_activity(self):
        self.client.force_login(self.user)

        # with self.assertRaises(PermissionDenied):
        response = self.client.put(
            reverse('effort-detail', kwargs={'pk': self.eff1.pk}),
            {
            'caption': 'new caption',
            'activity': self.activity.pk
            },
            format='json'
        )
        self.eff1.caption = 'new caption'
        serialized = EffortSerializer(self.eff1)

        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetAllEffortTest(BaseViewTest):

    def test_get_all_not_auth(self):
        """
        This test ensures that all Activity added in the setUp method
        exist when we make a GET request to the Activity/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(reverse("effort-list"))
        # fetch the data from db
        expected = Effort.objects.all()
        serialized = EffortSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_auth(self):
        self.client.force_login(self.user)
        # hit the API endpoint
        response = self.client.get(reverse("effort-list"))
        # fetch the data from db
        expected = Effort.objects.all()
        serialized = EffortSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
