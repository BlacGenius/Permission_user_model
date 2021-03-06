from rest_framework import serializers
from mainapp.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("title", "content", "user")
        read_only_fields = ("user", )
        