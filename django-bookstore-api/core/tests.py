import json
from django.test import TestCase
from core.models import Book

class BookstoreApiTests(TestCase):
    def test_search(self):
        Book.objects.create(title="Dune", author="Frank Herbert", year=1965)
        Book.objects.create(title="Neuromancer", author="William Gibson", year=1984)
        response = self.client.get("/books", {"q": "dune"})
        self.assertEqual(response.json()["total"], 1)
        created = self.client.post("/books", data=json.dumps({"title": "Hyperion", "author": "Dan Simmons", "year": 1989}), content_type="application/json")
        self.assertEqual(created.status_code, 201)
