import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Issue

def health(request):
    return JsonResponse({"status": "ok"})

def _issue(issue):
    return {"id": issue.id, "title": issue.title, "description": issue.description, "open": issue.open}

@csrf_exempt
def issues(request):
    if request.method == "POST":
        data = json.loads(request.body or b"{}")
        issue = Issue.objects.create(title=data.get("title", ""), description=data.get("description", ""))
        return JsonResponse(_issue(issue), status=201)
    return JsonResponse({"items": [_issue(i) for i in Issue.objects.order_by("-id")]})

@csrf_exempt
def close_issue(request, pk):
    try:
        issue = Issue.objects.get(pk=pk)
    except Issue.DoesNotExist:
        return JsonResponse({"error": "Issue not found"}, status=404)
    issue.open = False
    issue.save()
    return JsonResponse(_issue(issue))
