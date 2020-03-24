from django.test import TestCase
from django.urls import reverse
from rest_framework.test import (APITestCase,
    APIClient)

from rest_framework.exceptions import PermissionDenied

from rest_framework.views import status
from whatDo.models import Activity
from whatDo.serializers import ActivitySerializer
from accounts.models import User

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_activity(name, description, user):
        if name != "" and description != "" and user != None:
            return Activity.objects.create(
                name=name,
                description=description,
                created_by=user)

    def setUp(self):
        self.user = User.objects.create_user("user1@example.com", "p@ssw0rd")
        self.user2 = User.objects.create_user("user2@example.com", "p@ssw0rd")

        self.activity = self.create_activity("bake japanese cheescake",
            "cheescake", self.user2)
        self.create_activity("paint", "paint stary stary night",
            self.user2)
        self.create_activity("dance", "create a new dance", self.user2)
        self.create_activity("learn piano",
            "play river flows in you", self.user2)

class UpdateActivityTest(BaseViewTest):

    def test_not_creator_update_activity(self):
        self.client.force_login(self.user)
        print(self.user)
        print(self.activity.created_by)

        response = self.client.put(
            reverse('activity-detail', kwargs={'pk': self.activity.pk}),
            {'name': 'new name'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_creator_update_activity(self):
        self.client.force_login(self.user2)

        response = self.client.put(
            reverse('activity-detail', kwargs={'pk': self.activity.pk}),
            {'name': 'new name'},
            format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

class GetAllActivityTest(BaseViewTest):

    def test_get_all_not_auth(self):
        """
        This test ensures that all Activity added in the setUp method
        exist when we make a GET request to the Activity/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(reverse("activity-list"))
        # fetch the data from db
        expected = Activity.objects.all()
        serialized = ActivitySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_auth(self):
        self.client.force_login(self.user)
        # hit the API endpoint
        response = self.client.get(reverse("activity-list"))
        # fetch the data from db
        expected = Activity.objects.all()
        serialized = ActivitySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
