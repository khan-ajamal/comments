from django.db import models


class Comment(models.Model):
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Reply(models.Model):
    text = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name='replies'
    )
