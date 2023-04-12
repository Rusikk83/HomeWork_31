import json

from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.http import JsonResponse

from django.utils.decorators import method_decorator

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from HomeWork_27 import settings
from ads.models import User

'''представления для пользователя'''

class UserListView(ListView):
    model = User


    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        user_qs = self.object_list.annotate(total_ads=Count("ads", filter=Q(ads__is_published=True)))

        paginator = Paginator(user_qs.order_by("username"), settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)


        users = []

        for user in page_obj:
            users.append({
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "username": user.username,
                "password": '*' * len(user.password),
                "role": user.role,
                "age": user.age,
                "location": user.location.name,
                "total_ads": user.total_ads,
            })

        response = {
            'items': users,
            'num_pages': paginator.num_pages,
            'total': paginator.count
        }
        return JsonResponse(response, safe=False)


class UsersDetailView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        user = self.get_object()

        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": '*' * len(user.password),
            "role": user.role,
            "age": user.age,
            "location": user.location.name,

        })


@method_decorator(csrf_exempt, name="dispatch")
class UsersCreateView(CreateView):
    model = User

    fields = ['first_name', "last_name", 'username', 'password', 'role', 'age', "location_id"]

    def post(self, request, *args, **kwargs):
        user_data = json.loads(request.body)
        user = User.objects.create(
        first_name = user_data["first_name"],
        last_name = user_data["last_name"],
        username = user_data["username"],
        password = user_data["password"],
        role = user_data["role"],
        age = user_data["age"],
        location_id = user_data["location_id"],
        )


        return JsonResponse({
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "username": user.username,
            "password": '*' * len(user.password),
            "role": user.role,
            "age": user.age,
            "location_id": user.location_id,

        },
            status=201)


@method_decorator(csrf_exempt, name="dispatch")
class UsersUpdateView(UpdateView):
    model = User

    fields = ['first_name', "last_name", 'username', 'password',  'age', "location"]

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)
        user_data = json.loads(request.body)
        self.object.first_name = user_data["first_name"]
        self.object.last_name = user_data["last_name"]
        self.object.username = user_data["username"]
        self.object.password = user_data["password"]

        self.object.age = user_data["age"]
        self.object.location_id = user_data["location_id"]

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "first_name": self.object.first_name,
            "last_name": self.object.last_name,
            "username": self.object.username,
            "password": '*' * len(self.object.password),
            "role": self.object.role,
            "age": self.object.age,
            "location_id": self.object.location_id,

        },
            status=201)


@method_decorator(csrf_exempt, name="dispatch")
class UsersDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)

