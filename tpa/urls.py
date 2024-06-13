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
    path('', views.index, name='tpa_index'),
    path('create/', views.create, name='tpa_create'),
    path('update/<int:id>/', views.update, name='tpa_update'),
    path('delete/<int:id>/', views.delete, name='tpa_delete'),
]
