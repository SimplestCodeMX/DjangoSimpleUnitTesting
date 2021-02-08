from django.test import TestCase
from accounts.models import User


class TestModels(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username="test_user_token",
            first_name="TestUser"
        )

    def test_create_user(self):
        user = User.objects.create(
            username="test_user",
            first_name="TestUser"
        )
        self.assertEqual(str(user), "test_user")

    def test_access_token(self):
        self.assertIsNot(self.user.access_token, None, "Token Not Exists")


