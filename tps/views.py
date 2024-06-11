from django.shortcuts import render, get_object_or_404, redirect
from .models import Tps
from django.utils.crypto import get_random_string
from users.models import Users
from trash_place.models import TrashPlace
from tpa.models import Tpa

def index(request):
    tps = Tps.objects.select_related('trash_place', 'tpa').all()
    return render(request, 'pages/tps/index.html', {'tps': tps})


def create(request):
    if request.method == 'POST':
        kode_transaksi = get_random_string(10)
        trash_place_id = request.POST.get('trash_place_id')
        berat_sampah = request.POST.get('berat_sampah')
        tanggal = request.POST.get('tanggal')
        user_id = request.POST.get('user_id')

        trash_place = TrashPlace.objects.get(id=trash_place_id)
        user = Users.objects.get(id=user_id)

        tps = Tps(
            kode_transaksi=kode_transaksi,
            trash_place=trash_place,
            tanggal=tanggal,
            berat_sampah=berat_sampah,
            user=user,
        )
        tps.save()
        return redirect('tps_index')
    else:
        tempat_sampah = TrashPlace.objects.all()
        pengguna = Users.objects.all()
        return render(request, 'pages/tps/create.html', {
            'tempat_sampah': tempat_sampah,
            'pengguna': pengguna,
        })
        
def update(request, id):
    tps = get_object_or_404(Tps, id=id)
    if request.method == 'POST':
        tempat_sampah_id = request.POST.get('tempat_sampah')
        berat_sampah = request.POST.get('berat_sampah')
        pengguna_id = request.POST.get('pengguna')

        tps.tempat_sampah = TrashPlace.objects.get(id=tempat_sampah_id)
        tps.berat_sampah = berat_sampah
        tps.pengguna = Users.objects.get(id=pengguna_id)
        tps.save()
        return redirect('tps_index')
    else:
        tempat_sampah = TrashPlace.objects.all()
        pengguna = Users.objects.all()
        return render(request, 'pages/tps/update.html', {
            'tps': tps,
            'tempat_sampah': tempat_sampah,
            'pengguna': pengguna,
        })

def delete(request, id):
    tps = get_object_or_404(Tps, id=id)
    if request.method == 'POST':
        tps.delete()
        return redirect('tps_index')
    return render(request, 'tps/delete.html', {'tps': tps})

def process_landfill(request, id):
    tps = get_object_or_404(Tps, id=id)
    if request.method == 'POST':
        tpa_id = request.POST.get('tpa_id')
        tpa = get_object_or_404(Tpa, id=tpa_id)
        tps.tpa = tpa
        tps.save()
        return redirect('tps_index')
    else:
        tpa = Tpa.objects.all()
        return render(request, 'pages/tps/process_landfill.html', {
            'tps': tps,
            'tpa': tpa,
        })
        
def detail(request, id):
    tps = get_object_or_404(Tps, id=id)
    return render(request, 'pages/tps/detail.html', {'tps': tps})


