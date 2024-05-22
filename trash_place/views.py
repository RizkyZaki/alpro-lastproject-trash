"""

Kelas = SI4706
Kelompok = 11
Anggota Kelompok
1. Rizky Zaki Zulkarnaen 102022300080
https://zach-me.vercel.app

"""
from django.shortcuts import render, redirect
from .models import TrashPlace
from .forms import TrashPlaceForm

def index(request):
    trash_place = TrashPlace.objects.all()
    return render(request, 'pages/trash_place/index.html', {'trash_place': trash_place})

# Prepare Form