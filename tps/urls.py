from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='tps_index'),
    path('create/', views.create, name='tps_create'),
    path('update/<int:id>/', views.update, name='tps_update'),
    path('delete/<int:id>/', views.delete, name='tps_delete'),
    path('landfill/<int:id>/', views.process_landfill, name='process_landfill'),
    path('detail/<int:id>/', views.detail, name='trash_detail'),
]
