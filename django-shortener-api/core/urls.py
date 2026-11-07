from django.urls import path
from . import views
urlpatterns = [
    path("health", views.health),
    path("shorten", views.shorten),
    path("go/<slug:code>", views.follow),
]
