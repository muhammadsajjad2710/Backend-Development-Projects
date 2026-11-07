import json
from django.test import TestCase

class ShortenerApiTests(TestCase):
    def test_shorten_and_redirect(self):
        created = self.client.post("/shorten", data=json.dumps({"code": "docs", "url": "https://example.com/django"}), content_type="application/json")
        self.assertEqual(created.status_code, 201)
        response = self.client.get("/go/docs")
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response["Location"], "https://example.com/django")
