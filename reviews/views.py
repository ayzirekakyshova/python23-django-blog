from rest_framework.viewsets import ModelViewSet

from .models import Comment
from .serializer import CommentSerializer

class CommetViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer