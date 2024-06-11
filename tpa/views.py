from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tpa

def index(request):
    tpa = Tpa.objects.all()
    return render(request, 'pages/tpa/index.html', {'tpa': tpa})

def create(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        alamat = request.POST.get('alamat')
        keterangan = request.POST.get('keterangan')
        
        Tpa.objects.create(
            nama=nama,
            alamat=alamat,
            keterangan=keterangan,
        )
        return redirect('tpa_index')
    return render(request, 'pages/tpa/create.html')

def update(request, id):
    tpa = get_object_or_404(Tpa, id=id)
    if request.method == 'POST':
        Tpa.nama = request.POST.get('nama')
        Tpa.alamat = request.POST.get('alamat')
        Tpa.keterangan = request.POST.get('keterangan')
        
        Tpa.save()
        return redirect('tpa_index')
    return render(request, 'pages/tpa/update.html', {'tpa': tpa})

def delete(request, id):
    tpa = get_object_or_404(Tpa, id=id)
    if request.method == 'POST':
        Tpa.delete()
        return redirect('tpa_index')
    return render(request, 'pages/tpa/delete.html', {'tpa': tpa})
