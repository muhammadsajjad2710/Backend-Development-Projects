import json
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Book

def health(request):
    return JsonResponse({"status": "ok"})

@csrf_exempt
def books(request):
    if request.method == "POST":
        data = json.loads(request.body or b"{}")
        book = Book.objects.create(title=data.get("title", ""), author=data.get("author", ""), year=int(data.get("year") or 2000))
        return JsonResponse({"id": book.id, "title": book.title, "author": book.author, "year": book.year}, status=201)
    q = request.GET.get("q", "").strip()
    page = max(int(request.GET.get("page") or 1), 1)
    size = min(max(int(request.GET.get("size") or 10), 1), 50)
    qs = Book.objects.all().order_by("title")
    if q:
        qs = qs.filter(Q(title__icontains=q) | Q(author__icontains=q))
    start = (page - 1) * size
    items = list(qs[start:start + size].values("id", "title", "author", "year"))
    return JsonResponse({"total": qs.count(), "page": page, "size": size, "items": items})
