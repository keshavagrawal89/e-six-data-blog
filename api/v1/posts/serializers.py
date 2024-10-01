from rest_framework import serializers
from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        read_only_fields = ['uuid', 'created_on', 'updated_on', 'author']
        fields = ['uuid', 'title', 'content', 'author', 'created_on', 'updated_on']


    def get_author(self, value):
        return {
            'email': value.author.email,
            'name': value.author.first_name,
            'joined': value.author.created_on
        }
