from django.urls import path
from . import views
urlpatterns = [
    path("health", views.health),
    path("issues", views.issues),
    path("issues/<int:pk>/close", views.close_issue),
]
