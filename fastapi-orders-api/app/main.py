from __future__ import annotations
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class ItemIn(BaseModel):
    sku: str = Field(min_length=1, max_length=32)
    quantity: int = Field(gt=0)
    price_cents: int = Field(gt=0)

class OrderIn(BaseModel):
    customer: str = Field(min_length=1, max_length=80)
    items: list[ItemIn] = Field(min_length=1)

def create_app() -> FastAPI:
    app = FastAPI(title="Orders API", version="1.0.0")
    app.state.orders = {}
    app.state.next_id = 1

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.post("/orders", status_code=201)
    def create_order(payload: OrderIn):
        total = sum(item.quantity * item.price_cents for item in payload.items)
        order = {
            "id": app.state.next_id,
            "customer": payload.customer,
            "status": "open",
            "items": [item.model_dump() for item in payload.items],
            "total_cents": total,
        }
        app.state.next_id += 1
        app.state.orders[order["id"]] = order
        return order

    @app.get("/orders")
    def list_orders():
        return list(app.state.orders.values())

    @app.get("/orders/{order_id}")
    def get_order(order_id: int):
        if order_id not in app.state.orders:
            raise HTTPException(404, "Order not found")
        return app.state.orders[order_id]

    @app.post("/orders/{order_id}/cancel")
    def cancel_order(order_id: int):
        order = app.state.orders.get(order_id)
        if order is None:
            raise HTTPException(404, "Order not found")
        if order["status"] != "open":
            raise HTTPException(409, "Order cannot be cancelled")
        order["status"] = "cancelled"
        return order

    return app

app = create_app()
