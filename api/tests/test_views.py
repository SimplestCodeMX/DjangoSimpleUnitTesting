from django.test import TestCase
from django.conf import settings

from accounts.models import User


class TestApiViews(TestCase):

    def test_get_no_users(self):
        response = self.client.get(f"/api/")
        self.assertEqual(response.status_code, 200, 'Status Wrong')
        self.assertDictEqual(
            response.json(),
            {
                'count': 0, 'next': None, 'previous': None, 'results': []
            },
            "Wrong Response"
        )
        self.assertEqual(response.json().get('count'), 0, "Wrong Count Value")

    def test_get_users(self):
        User.objects.create(**{"username": "goduser", "password": "1234567890"})
        response = self.client.get(f"/api/")
        self.assertEqual(response.status_code, 200, 'Status Wrong')
        self.assertListEqual(
            list(response.json().keys()),
            ["count", "next", "previous", "results"],
            "Wrong Response"
        )
        self.assertEqual(len(response.json().get("results")), 1, "Wrong Count Value")

    def test_get_user_detail(self):
        user = User.objects.create(**{"username": "goduser2", "password": "1234567890"})
        response = self.client.get(f"/api/{user.id}")
        self.assertEqual(response.status_code, 200, 'Status Wrong')
        self.assertIs(response.json(), dict, "Wrong Response")
        self.assertEqual(len(response.json().get("results")), 1, "Wrong Count Value")
