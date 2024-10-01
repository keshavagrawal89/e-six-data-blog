from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


from api.v1.posts.filters import PostFilter
from api.v1.posts.permissons import IsOwnerOrReadOnly
from posts.models import Post
from api.v1.posts.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filterset_class = PostFilter
    ordering_fields = ['created_on']
    ordering = ['-created_on']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
