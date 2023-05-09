import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.decorators import permission_classes
from rest_framework.generics import RetrieveAPIView, CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated

from HomeWork_27 import settings
from ads.models import Ads, Categories, User, Location
from ads.permissions.permissions import IsModerator, IsAuthor
from ads.serializers.ad_serialize import AdsDetailSerializer, AdsCreateSerializer, AdsUpdateSerializer


# Create your views here.
def root(request):
    return JsonResponse({"status": "ok"}, status=200)



class AdsListView(ListView):
    model = Ads


    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        name_filter = request.GET.get('text')  # получаем из запроса значание фильтра по имени
        category_filter = request.GET.get('cat')
        location_filter = request.GET.get('location')
        price_from_filter = request.GET.get('price_from')
        price_to_filter = request.GET.get('price_to')

        if name_filter:
            self.object_list = self.object_list.filter(name__contains=name_filter)  # фильтр по названию

        if category_filter:
            self.object_list = self.object_list.filter(category_id=category_filter)  # фильтр по категории

        if price_from_filter:
            self.object_list = self.object_list.filter(price__gte=price_from_filter)  # фильтр по нижней цене

        if price_to_filter:
            self.object_list = self.object_list.filter(price__lte=price_to_filter)  # фильтр по верхней цене

        if location_filter:
            self.object_list = self.object_list.filter(author__location__name__icontains=location_filter)  # это не работает



        paginator = Paginator(self.object_list.order_by('name'), settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ads = []

        for ad in page_obj:
            ads.append({
                "id": ad.id,
                "name": ad.name,
                "author_id": ad.author_id,
                "price": ad.price,
                "description": ad.description,
                "category_id": ad.category_id,
                "is_published": ad.is_published,
                "image": ad.image.url if ad.image else None,
            })

        response = {
            'items': ads,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }
        return JsonResponse(response, safe=False)


class AdsDetailView(RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsDetailSerializer
    permission_classes = [IsAuthenticated]


class AdsCreateView(CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsCreateSerializer
    #permission_classes = [IsAuthenticated]



class AdsUpdateView(UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsUpdateSerializer
    permission_classes = [IsAuthenticated, IsAuthor | IsModerator]  #проверка прав: авторизован, модератор или владелец


class AdsDeleteView(DestroyAPIView):
    queryset = Ads.objects.all()
    permission_classes = [IsAuthenticated, IsAuthor | IsModerator]  #проверка прав: авторизован, модератор или владелец




@method_decorator(csrf_exempt, name="dispatch")
class AdsUploadImageView(UpdateView):
    model = Ads
    fields = ['image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES['image']
        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name":self.object.name,
            "author": self.object.author_id,
            "price": self.object.price,
            "description": self.object.description,
            "category": self.object.category_id,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None,
        },
            status=201)







