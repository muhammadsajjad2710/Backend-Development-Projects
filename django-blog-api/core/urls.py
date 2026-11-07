from django.urls import path
from . import views
urlpatterns = [
    path("health", views.health),
    path("posts", views.posts),
    path("posts/<int:pk>", views.post_detail),
    path("posts/<int:pk>/comments", views.comments),
]
