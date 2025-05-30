"""Models for Comments App."""

from datetime import datetime
from mongoengine import (
    Document,
    StringField,
    ReferenceField,
    DateTimeField,
    ListField,
    CASCADE,
)


class Post(Document):
    """Model definition for Post."""

    title = StringField(required=True)
    content = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)


class Comment(Document):
    """Model definition for Comment."""

    post = ReferenceField(Post, reverse_delete_rule=CASCADE)
    parent = ReferenceField("self", null=True, default=None)
    author = StringField(required=True)
    text = StringField(required=True)
    created_at = DateTimeField(default=datetime.utcnow)
    replies = ListField(ReferenceField("self"))

    def add_reply(self, reply_comment) -> None:
        self.replies.append(reply_comment)
        self.save()
