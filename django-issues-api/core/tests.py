import json
from django.test import TestCase

class IssueApiTests(TestCase):
    def test_open_and_close(self):
        created = self.client.post("/issues", data=json.dumps({"title": "Login 500", "description": "crash"}), content_type="application/json")
        pk = created.json()["id"]
        closed = self.client.post(f"/issues/{pk}/close")
        self.assertFalse(closed.json()["open"])
