"""URLs for Comments App."""

from django.urls import path
from django.urls.resolvers import URLPattern

from .views import (
    PostListCreateView,
    CommentListCreateView,
)

urlpatterns: list[URLPattern] = [
    path(
        "api/posts",
        PostListCreateView.as_view(),
        name="posts",
    ),
    path(
        "api/posts/<post_id>/comments",
        CommentListCreateView.as_view(),
        name="comments",
    ),
]
