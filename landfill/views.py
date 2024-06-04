from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Landfill

def index(request):
    landfill = Landfill.objects.all()
    return render(request, 'pages/landfill/index.html', {'landfill': landfill})

def create(request):
    if request.method == 'POST':
        nama = request.POST.get('nama')
        alamat = request.POST.get('alamat')
        keterangan = request.POST.get('keterangan')
        
        Landfill.objects.create(
            nama=nama,
            alamat=alamat,
            keterangan=keterangan,
        )
        return redirect('landfill_index')
    return render(request, 'pages/landfill/create.html')

def update(request, id):
    landfill = get_object_or_404(Landfill, id=id)
    if request.method == 'POST':
        landfill.nama = request.POST.get('nama')
        landfill.alamat = request.POST.get('alamat')
        landfill.keterangan = request.POST.get('keterangan')
        
        landfill.save()
        return redirect('landfill_index')
    return render(request, 'pages/landfill/update.html', {'landfill': landfill})

def delete(request, id):
    landfill = get_object_or_404(Landfill, id=id)
    if request.method == 'POST':
        landfill.delete()
        return redirect('landfill_index')
    return render(request, 'pages/landfill/delete.html', {'landfill': landfill})
