from rest_framework import serializers

from ads.models import Ad, Category, Selection
from users.models import User


def is_published_validator(value):
    if value:
        raise serializers.ValidationError('is_published cannot be True')
    return value


class AdListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"

class AdCreateSerializer(serializers.ModelSerializer):
    is_published = serializers.BooleanField(validators=[is_published_validator], required=False)
    class Meta:
        model = Ad
        fields = "__all__"

class AdDetailSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Ad
        fields = "__all__"


class AdUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"


class SelectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = "__all__"



class SelectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Selection
        fields = ['id', 'name']


class SelectionDetailSerializer(serializers.ModelSerializer):
    items = AdListSerializer(many=True)

    class Meta:
        model = Selection
        fields = "__all__"
