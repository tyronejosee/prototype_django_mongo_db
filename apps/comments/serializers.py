"""Serializers for Comments App."""

from rest_framework import serializers

from .models import Post, Comment


class PostSerializer(serializers.Serializer):
    """Serializer for posts."""

    id = serializers.CharField(read_only=True)
    title = serializers.CharField()
    content = serializers.CharField()

    def create(self, validated_data) -> Post:
        return Post(**validated_data).save()


class RecursiveCommentSerializer(serializers.Serializer):
    """Serializer for recursive comments."""

    id = serializers.CharField(read_only=True)
    author = serializers.CharField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField()
    replies = serializers.ListSerializer(
        child=serializers.DictField(),
        required=False,
    )


class CommentSerializer(serializers.Serializer):
    """Serializer for comments."""

    id = serializers.CharField(read_only=True)
    post = serializers.CharField()
    parent = serializers.CharField(required=False, allow_null=True)
    author = serializers.CharField()
    text = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)

    def to_representation(self, instance) -> dict:
        data = super().to_representation(instance)
        data["replies"] = [
            RecursiveCommentSerializer(reply).data for reply in instance.replies
        ]
        return data

    def create(self, validated_data) -> Comment:
        post_id = validated_data.pop("post")
        parent_id = validated_data.pop("parent", None)

        post = Post.objects.get(id=post_id)
        comment = Comment(post=post, **validated_data)

        if parent_id:
            parent_comment = Comment.objects.get(id=parent_id)
            comment.parent = parent_comment

        comment.save()

        if comment.parent:
            comment.parent.add_reply(comment)

        return comment
