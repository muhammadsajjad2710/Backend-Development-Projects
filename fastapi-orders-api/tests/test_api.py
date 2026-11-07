from fastapi.testclient import TestClient
from app.main import create_app

def test_create_and_cancel_order():
    client = TestClient(create_app())
    created = client.post("/orders", json={
        "customer": "Aisha",
        "items": [{"sku": "MUG", "quantity": 2, "price_cents": 499}],
    }).json()
    assert created["total_cents"] == 998
    cancelled = client.post(f"/orders/{created['id']}/cancel").json()
    assert cancelled["status"] == "cancelled"
    assert client.get("/orders/99").status_code == 404
