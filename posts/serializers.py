from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "body",
            "date",
            "author"
        ]

        read_only_fields = ["id", "date", "author"]

    def get_author(self, obj):
        return str(obj.author)
