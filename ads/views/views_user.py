import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView, DeleteView
from rest_framework.generics import RetrieveAPIView, ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import User, Location
from ads.serializers.user_serialize import UserDetailSerializer, UserCreateSerializer

'''представления для пользователя'''

class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UsersDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer




@method_decorator(csrf_exempt, name="dispatch")
class UsersCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        location = get_object_or_404(Location, id=self.request.data.get('location_id'))
        return serializer.save(location=location)


@method_decorator(csrf_exempt, name="dispatch")
class UsersUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    '''Без этого кода не обновляется location_id, а с этим кодом не работает частичное обновление'''
    # def perform_update(self, serializer):
    #     location = get_object_or_404(Location, id=self.request.data.get('location_id'))
    #     return serializer.save(location=location)


@method_decorator(csrf_exempt, name="dispatch")
class UsersDeleteView(DestroyAPIView):
    queryset = User.objects.all()




