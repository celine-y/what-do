from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Activity
from .serializers import ActivitySerializer

# tests for views

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_activity(name="", description=""):
        if name != "" and description != "":
            Activity.objects.create(name=name, description=description)

    def setUp(self):
        # add test data
        self.create_activity("bake japanese cheesecake", "recipe for creating japanese cheescake")
        self.create_activity("paint", "paint stary stary night")
        self.create_activity("dance", "create a new dance")
        self.create_activity("learn piano", "play river flows in you")


class GetAllActivityTest(BaseViewTest):

    def test_get_all_activity(self):
        """
        This test ensures that all Activity added in the setUp method
        exist when we make a GET request to the Activity/ endpoint
        """
        # hit the API endpoint
        response = self.client.get(
            reverse("activity-all", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Activity.objects.all()
        serialized = ActivitySerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
