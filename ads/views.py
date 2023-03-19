import json

from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, Categories


# Create your views here.
def root(request):
    return JsonResponse({"status": "ok"}, status=200)


@method_decorator(csrf_exempt, name="dispatch")
class AdsView(View):
    def get(self, request):

        ads = Ads.objects.all()
        response = []

        for ad in ads:
            response.append({
                "id": ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published,
            })
        return JsonResponse(response, safe=False)


    def post(self, request):
        ad_data = json.loads(request.body)
        ad = Ads()
        ad.name = ad_data["name"]
        ad.author = ad_data["author"]
        ad.price = ad_data["price"]
        ad.description = ad_data["description"]
        ad.address = ad_data["address"]
        ad.is_published = ad_data["is_published"]

        ad.save()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        },
            status=201)




@method_decorator(csrf_exempt, name="dispatch")
class CatView(View):
    def get(self, request):
        categories = Categories.objects.all()
        response = []

        for categorie in categories:
            response.append({
                "id": categorie.id,
                "name": categorie.name
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)
        cat = Categories()
        cat.name = cat_data["name"]

        cat.save()

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        },
            status=201)


class AdsDetailView(DetailView):
    model = Ads
    def get(self, request, *args, **kwargs):

        ad = self.get_object()

        return JsonResponse({
            "id": ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,

        })


class CatDetailView(DetailView):
    model = Categories
    def get(self, request, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        })



