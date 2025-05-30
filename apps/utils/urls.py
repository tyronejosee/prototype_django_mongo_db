"""URLs for Utils App."""

from django.urls import path
from django.urls.resolvers import URLPattern

from .views import MongoHealthCheckView

urlpatterns: list[URLPattern] = [
    path(
        "api/health",
        MongoHealthCheckView.as_view(),
        name="health",
    ),
]
