from rest_framework import serializers

from ads.models import Ads


class AdsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ads

        fields = '__all__'