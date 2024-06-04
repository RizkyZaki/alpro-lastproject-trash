from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='landfill_index'),
    path('create/', views.create, name='landfill_create'),
    path('update/<int:id>/', views.update, name='landfill_update'),
    path('delete/<int:id>/', views.delete, name='landfill_delete'),
]
