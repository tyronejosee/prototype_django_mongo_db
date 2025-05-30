"""Views for Comments App."""

from django.db.models import QuerySet
from rest_framework import generics

from .models import Comment, Post
from .serializers import PostSerializer, CommentSerializer


class PostListCreateView(generics.ListCreateAPIView):
    """View for posts."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListCreateView(generics.ListCreateAPIView):
    """View for comments."""

    serializer_class = CommentSerializer

    def get_queryset(self) -> QuerySet:
        post_id = self.kwargs["post_id"]
        return Comment.objects.filter(post=post_id, parent=None)
