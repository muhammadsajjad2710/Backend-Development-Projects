import json
from django.test import TestCase
from core.models import Product

class InventoryApiTests(TestCase):
    def test_sell(self):
        product = Product.objects.create(name="Mug", stock=5, price_cents=499)
        sold = self.client.post(f"/products/{product.pk}/sell", data=json.dumps({"quantity": 2}), content_type="application/json")
        self.assertEqual(sold.json()["remaining"], 3)
        fail = self.client.post(f"/products/{product.pk}/sell", data=json.dumps({"quantity": 9}), content_type="application/json")
        self.assertEqual(fail.status_code, 409)
