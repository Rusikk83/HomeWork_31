from rest_framework.serializers import ModelSerializer

from ads.models import Categories


class CatSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Categories
