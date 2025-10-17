from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model
from tasks.models import Task

User = get_user_model()

class TaskTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username="tester", password="testpass123", email="t@example.com")
        r = self.client.post("/api/users/login/", {"username":"tester","password":"testpass123"}, format="json")
        self.assertEqual(r.status_code, 200)
        token = r.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")

    def test_create_and_complete_task(self):
        payload = {"title":"Test Task","description":"desc"}
        create = self.client.post("/api/tasks/", payload, format="json")
        self.assertEqual(create.status_code, 201)
        task_id = create.data["id"]
        complete = self.client.patch(f"/api/tasks/{task_id}/complete/", format="json")
        self.assertEqual(complete.status_code, 200)
        t = Task.objects.get(id=task_id)
        self.assertEqual(t.status, Task.STATUS_COMPLETED)
