from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='category_index'),
    path('create/', views.create, name='category_create'),
    path('update/<int:id>/', views.update, name='category_update'),
    path('delete/<int:id>/', views.delete, name='category_delete'),
]
