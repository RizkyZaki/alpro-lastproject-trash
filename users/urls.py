"""

Kelas = SI4706
Kelompok = 11
Anggota Kelompok
1. Rizky Zaki Zulkarnaen 102022300080
https://zach-me.vercel.app

"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('create/', views.create, name='user_create'),
    path('update/<int:id>/', views.update, name='user_update'),
    path('delete/<int:id>/', views.delete, name='user_delete'),
    path('reset_password/<int:id>/', views.reset_password, name='user_reset_password'),
]