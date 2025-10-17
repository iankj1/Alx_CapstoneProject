
from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_and_login(self):
        payload = {"username":"tester","email":"t@example.com","password":"strongpass123","password2":"strongpass123"}
        res = self.client.post("/api/users/register/", payload, format="json")
        self.assertEqual(res.status_code, 201)
        login = self.client.post("/api/users/login/", {"username":"tester","password":"strongpass123"}, format="json")
        self.assertEqual(login.status_code, 200)
        self.assertIn("access", login.data)
