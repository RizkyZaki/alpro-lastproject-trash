"""

Kelas = SI4706
Kelompok = 11
Anggota Kelompok
1. Rizky Zaki Zulkarnaen 102022300080
https://zach-me.vercel.app

"""
from django.shortcuts import render, redirect, get_object_or_404
from .models import TrashPlace
from category.models import Category
from django.utils import timezone


def index(request):
    trash_places = TrashPlace.objects.select_related('category').all()
    return render(request, 'pages/trash_place/index.html', {'trash_places': trash_places})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        address = request.POST.get('address')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')

        # Validasi sederhana
        if not name or not category_id or not address or not longitude or not latitude:
            return render(request, 'pages/trash_place/create.html', {'error': 'All fields are required', 'categories': Category.objects.all()})

        # Simpan data ke dalam model TrashPlace
        trash_place = TrashPlace.objects.create(
            name=name,
            category_id=category_id,
            address=address,
            longitude=longitude,
            latitude=latitude,
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

        return redirect('trash_place_index')
    else:
        categories = Category.objects.all()
        return render(request, 'pages/trash_place/create.html', {'categories': categories})
    
def update(request, id):
    trash_place = get_object_or_404(TrashPlace, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        category_id = request.POST.get('category')
        address = request.POST.get('address')
        longitude = request.POST.get('longitude')
        latitude = request.POST.get('latitude')

        # Validasi sederhana
        if not name or not category_id or not address or not longitude or not latitude:
            return render(request, 'pages/trash_place/update.html', {'error': 'All fields are required', 'trash_place': trash_place})

        # Update data TrashPlace
        trash_place.name = name
        trash_place.category_id = category_id
        trash_place.address = address
        trash_place.longitude = longitude
        trash_place.latitude = latitude
        trash_place.save()

        return redirect('trash_place_index')
    else:
        return render(request, 'pages/trash_place/update.html', {'trash_place': trash_place})

def delete(request, id):
    trash_place = get_object_or_404(TrashPlace, id=id)
    if request.method == 'POST':
        trash_place.delete()
        return redirect('trash_place_index')
    return render(request, 'pages/trash_place/delete.html', {'trash_place': trash_place})