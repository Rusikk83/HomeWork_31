from ads.views import views_user

from django.urls import path

urlpatterns = [

    path('', views_user.UserListView.as_view()),
    path('<int:pk>/update/', views_user.UsersUpdateView.as_view()),
    path('<int:pk>/delete/', views_user.UsersDeleteView.as_view()),
    path('create/', views_user.UsersCreateView.as_view()),
    path('<int:pk>/', views_user.UsersDetailView.as_view()),
    ]
