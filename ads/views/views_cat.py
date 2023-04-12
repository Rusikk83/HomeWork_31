import json


from django.http import JsonResponse

from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView


from ads.models import Categories

'''представления для категорий'''


class CatListView(ListView):
    model = Categories

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        categories = self.object_list
        response = []

        for categorie in categories:
            response.append({
                "id": categorie.id,
                "name": categorie.name
            })
        return JsonResponse(response, safe=False)


class CatDetailView(DetailView):
    model = Categories
    def get(self, request, *args, **kwargs):
        cat = self.get_object()

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        })


@method_decorator(csrf_exempt, name="dispatch")
class CatCreateView(CreateView):
    model = Categories

    fields = ["name"]

    def post(self, request, *args, **kwargs):
        cat_data = json.loads(request.body)
        cat = Categories.objects.create(
            name = cat_data["name"]
        )


        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        },
            status=201)


@method_decorator(csrf_exempt, name="dispatch")
class CatUpdateView(UpdateView):
    model = Categories

    fields = ["name"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        cat_data = json.loads(request.body)

        self.object.name = cat_data["name"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
        },
            status=201)


@method_decorator(csrf_exempt, name="dispatch")
class CatDeleteView(DeleteView):
    model = Categories
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)

