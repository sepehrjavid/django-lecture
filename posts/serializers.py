from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from posts.models import Post, Rating


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    picture = serializers.SerializerMethodField()
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            "id",
            "title",
            "body",
            "picture",
            "date_time",
            "author",
            "rating"
        ]

        read_only_fields = ("id", "author")

    def get_author(self, obj):
        return obj.author.username

    def get_rating(self, obj):
        qs = Rating.objects.filter(post=obj)
        return RatingSerializer(qs, many=True).data

    def get_picture(self, obj):
        if obj.picture:
            return obj.picture.url
        return


class RatingSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = Rating
        fields = [
            "rate",
            "user"
        ]

        read_only_fields = ("user",)

    def validate_rate(self, value):
        if value < 0 or value > 5:
            raise ValidationError("rate should be between 0 and 5")
        return value

    def get_user(self, obj):
        return obj.user.username
