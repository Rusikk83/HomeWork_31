from ads.views import views_cat

from django.urls import path

urlpatterns = [


    path('', views_cat.CatListView.as_view()),
    path('<int:pk>/', views_cat.CatDetailView.as_view()),
    path('create/', views_cat.CatCreateView.as_view()),
    path('<int:pk>/update/', views_cat.CatUpdateView.as_view()),
    path('<int:pk>/delete/', views_cat.CatDeleteView.as_view()),
    ]
