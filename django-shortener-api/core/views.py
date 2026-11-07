import json
from django.http import JsonResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import ShortLink

def health(request):
    return JsonResponse({"status": "ok"})

@csrf_exempt
def shorten(request):
    data = json.loads(request.body or b"{}")
    link = ShortLink.objects.create(code=data.get("code", ""), url=data.get("url", ""))
    return JsonResponse({"code": link.code, "url": link.url, "short_path": f"/go/{link.code}"}, status=201)

def follow(request, code):
    try:
        link = ShortLink.objects.get(code=code)
    except ShortLink.DoesNotExist:
        return JsonResponse({"error": "Unknown code"}, status=404)
    return HttpResponseRedirect(link.url)
