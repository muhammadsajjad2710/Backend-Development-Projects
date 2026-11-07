import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Product

def health(request):
    return JsonResponse({"status": "ok"})

def _product(product):
    return {"id": product.id, "name": product.name, "stock": product.stock, "price_cents": product.price_cents}

@csrf_exempt
def products(request):
    if request.method == "POST":
        data = json.loads(request.body or b"{}")
        product = Product.objects.create(name=data.get("name", ""), stock=int(data.get("stock") or 0), price_cents=int(data.get("price_cents") or 1))
        return JsonResponse(_product(product), status=201)
    return JsonResponse({"items": [_product(p) for p in Product.objects.order_by("name")]})

@csrf_exempt
def sell(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return JsonResponse({"error": "Product not found"}, status=404)
    qty = int(json.loads(request.body or b"{}").get("quantity") or 1)
    if product.stock < qty:
        return JsonResponse({"error": "Insufficient stock"}, status=409)
    product.stock -= qty
    product.save()
    return JsonResponse({"sold": qty, "remaining": product.stock})
