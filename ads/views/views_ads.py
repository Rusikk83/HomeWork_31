import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from HomeWork_27 import settings
from ads.models import Ads, Categories, User, Location


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
            self.object_list = self.object_list.filter(author__location__name__icontans=location_filter)  # это не работает



        paginator = Paginator(self.object_list.order_by('name'), settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        ads = []

        for ad in page_obj:
            ads.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author_id,
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


class AdsDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author_id": ad.author_id,
            "price": ad.price,
            "description": ad.description,
            "category_id": ad.category_id,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,

        })


@method_decorator(csrf_exempt, name="dispatch")
class AdsCreateView(CreateView):
    model = Ads

    fields = ['name', "author_id", 'price', 'description', 'is_published', 'category_id']

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)
        ad = Ads.objects.create(
        name = ad_data["name"],
        author_id = ad_data["author_id"],
        price = ad_data["price"],
        description = ad_data["description"],
        category_id = ad_data["category_id"],

        is_published = ad_data["is_published"],
        )


        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author_id,
            "price": ad.price,
            "description": ad.description,
            "category": ad.category_id,
            "is_published": ad.is_published,

        },
            status=201)


@method_decorator(csrf_exempt, name="dispatch")
class AdsUpdateView(UpdateView):
    model = Ads

    fields = ['name', 'price', 'description', 'author',  'category']

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        ad_data = json.loads(request.body)
        self.object.name = ad_data["name"]

        self.object.price = ad_data["price"]
        self.object.description = ad_data["description"]
        self.object.category_id = ad_data["category_id"]

        self.object.author_id = ad_data["author_id"]

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


@method_decorator(csrf_exempt, name="dispatch")
class AdsDeleteView(DeleteView):
    model = Ads
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


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







