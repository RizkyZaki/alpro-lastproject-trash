"""
URL configuration for tubes_sampah project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
"""

Kelas = SI4706
Kelompok = 11
Anggota Kelompok
1. Rizky Zaki Zulkarnaen 102022300080
https://zach-me.vercel.app

"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='dashboard'),
    path('search/', views.search, name='search'),
    path('filter/', views.filter, name='filter'),
    # path('admin/', admin.site.urls),
    path('login/', views.user_login, name='login'),  
    path('logout/', views.user_logout, name='logout'),
    path('category/', include('category.urls')),
    path('trash-place', include('trash_place.urls')),
    path('user/', include('users.urls')),
    path('tpa/', include('tpa.urls')),
    path('tps/', include('tps.urls')),
]
