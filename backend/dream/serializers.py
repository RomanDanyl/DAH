from rest_framework import serializers
from dream.models import Dream, Comment, Contribution


class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = ['dream', 'user', 'description', 'date']


class DreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = ['name', 'description', 'image', 'cost', 'category', 'location', 'views']

    category = serializers.ChoiceField(choices=Dream.Category.choices)


class DreamReadSerializer(DreamSerializer):
    contributions = ContributionSerializer(many=True, read_only=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Dream
        fields = [
            'id',
            'name',
            'description',
            'image',
            'image_url',
            'user',
            'cost',
            'accumulated',
            'status',
            'category',
            'date_added',
            'location',
            'views',
            'contributions',
        ]

    def get_image_url(self, obj):
        if obj.image:
            return obj.image.url
        return None


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text']


class CommentReadSerializer(CommentSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at', 'likes']
