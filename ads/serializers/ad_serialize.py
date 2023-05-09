from rest_framework import serializers
from rest_framework.fields import BooleanField
from rest_framework.relations import SlugRelatedField

from ads.models import Ads, Categories, User
from ads.validators.ad_validators import check_is_published


class AdsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads

        fields = '__all__'


class AdsCreateSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field="username", queryset=User.objects.all())
    category = SlugRelatedField(slug_field="name", queryset=Categories.objects.all())

    is_published = BooleanField(validators=[check_is_published], required=False)


    class Meta:
        model = Ads

        exclude = ['image']


class AdsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads

        exclude = ['image', 'author']
