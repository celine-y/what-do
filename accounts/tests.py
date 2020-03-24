from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import User
from .serializers import UserSerializer

# Create your tests here.
class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(username="", password=""):
        if username != "" and password != "":
            User.objects.create(username=username, password=password)

    def setUp(self):
        # add test data
        self.create_user("user1", "pass1")


class UserLoginTest(BaseViewTest):

    def test_user_login(self):
        """
        Created user can login
        """
        # hit the API endpoint
        # response = self.client.get(
        #     reverse("Activity-all", kwargs={"version": "v1"})
        # )
        # # fetch the data from db
        # expected = Activity.objects.all()
        # serialized = ActivitySerializer(expected, many=True)
        # self.assertEqual(response.data, serialized.data)
        # self.assertEqual(response.status_code, status.HTTP_200_OK)
