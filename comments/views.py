from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from comments.models import Comment, Reply
from comments.serializers import CommentSerializer, ReplySerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

    @action(detail=True)
    def replies(self, request, *args, **kwargs):
        comment = self.get_object()
        replies = comment.replies.all()
        return Response(ReplySerializer(
            replies, many=True, context={"request": request}
        ).data)


class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all().order_by('-created_at')
    serializer_class = ReplySerializer
