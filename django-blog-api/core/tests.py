import json
from django.test import TestCase

class BlogApiTests(TestCase):
    def test_post_and_comment(self):
        created = self.client.post("/posts", data=json.dumps({"title": "Hello", "body": "World"}), content_type="application/json")
        self.assertEqual(created.status_code, 201)
        pk = created.json()["id"]
        comment = self.client.post(f"/posts/{pk}/comments", data=json.dumps({"author": "Bilal", "body": "Nice"}), content_type="application/json")
        self.assertEqual(comment.status_code, 201)
        detail = self.client.get(f"/posts/{pk}")
        self.assertEqual(detail.json()["comments"][0]["body"], "Nice")
