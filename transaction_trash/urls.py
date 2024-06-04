from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='transaction_trash_index'),
    path('create/', views.create, name='transaction_trash_create'),
    path('update/<int:id>/', views.update, name='transaction_trash_update'),
    path('delete/<int:id>/', views.delete, name='transaction_trash_delete'),
]