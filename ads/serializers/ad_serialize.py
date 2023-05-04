from rest_framework import serializers

from ads.models import Ads


class AdsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads

        fields = '__all__'


class AdsCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads

        exclude = ['image']


class AdsUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads

        exclude = ['image', 'author']
