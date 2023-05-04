from rest_framework.relations import SlugRelatedField
from rest_framework.serializers import ModelSerializer

from ads.models import User, Selection
from ads.serializers.ad_serialize import AdsDetailSerializer


class SelectionSerializer(ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Selection

class SelectionDetailSerializer(ModelSerializer):
    item = AdsDetailSerializer(many=True)

    class Meta:
        fields = "__all__"
        model = Selection


class SelectionListSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field='username', queryset=User.objects.all())


    class Meta:
        fields = ['owner', 'name']
        model = Selection


class SelectionCreateSerializer(ModelSerializer):
    owner = SlugRelatedField(slug_field='username', queryset=User.objects.all(), required=False)

    def create(self, validated_data):
        request = self.context.get("request")
        validated_data["owner"] = request.user
        return super().create(validated_data)

    class Meta:
        fields = "__all__"
        model = Selection
