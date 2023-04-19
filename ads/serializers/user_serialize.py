from rest_framework import serializers

from ads.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', "last_name", 'username',  'role', 'age', "location_id"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', "last_name", 'username', 'password', 'role', 'age', "location_id"]


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', "last_name", 'username', 'password', 'role', 'age', "location_id"]
