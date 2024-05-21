from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='category_index'),
    path('create/', views.create, name='category_create'),
]