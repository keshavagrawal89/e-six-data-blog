from django_filters import rest_framework as filters
from posts.models import Post


class PostFilter(filters.FilterSet):
    author = filters.CharFilter(field_name="author__first_name")
    
    class Meta:
        model = Post
        fields = ['is_active', 'author', 'created_on']
