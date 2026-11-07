import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Comment, Post

def _body(request):
    return json.loads(request.body or b"{}")

def _post(post):
    return {
        "id": post.id,
        "title": post.title,
        "body": post.body,
        "comments": [{"id": c.id, "author": c.author, "body": c.body} for c in post.comments.all()],
    }

def health(request):
    return JsonResponse({"status": "ok"})

@csrf_exempt
def posts(request):
    if request.method == "POST":
        data = _body(request)
        post = Post.objects.create(title=data.get("title", ""), body=data.get("body", ""))
        return JsonResponse(_post(post), status=201)
    return JsonResponse({"items": [_post(post) for post in Post.objects.order_by("-id")]})

@csrf_exempt
def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found"}, status=404)
    return JsonResponse(_post(post))

@csrf_exempt
def comments(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return JsonResponse({"error": "Post not found"}, status=404)
    data = _body(request)
    comment = Comment.objects.create(post=post, author=data.get("author", ""), body=data.get("body", ""))
    return JsonResponse({"id": comment.id, "author": comment.author, "body": comment.body}, status=201)
