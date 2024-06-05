from django.shortcuts import render, get_object_or_404, redirect
from .models import TrashTransaction
from django.utils.crypto import get_random_string
from users.models import Users
from trash_place.models import TrashPlace

def index(request):
    transactions = TrashTransaction.objects.select_related('trash_place', 'landfill').all()
    return render(request, 'pages/transaction_trash/index.html', {'transactions': transactions})


def create(request):
    if request.method == 'POST':
        kode_transaksi = get_random_string(10)
        trash_place_id = request.POST.get('trash_place_id')
        berat_sampah = request.POST.get('berat_sampah')
        tanggal = request.POST.get('tanggal')
        user_id = request.POST.get('user_id')

        trash_place = TrashPlace.objects.get(id=trash_place_id)
        user = Users.objects.get(id=user_id)

        transaction = TrashTransaction(
            kode_transaksi=kode_transaksi,
            trash_place=trash_place,
            tanggal=tanggal,
            berat_sampah=berat_sampah,
            user=user,
        )
        transaction.save()
        return redirect('transaction_trash_index')
    else:
        tempat_sampah = TrashPlace.objects.all()
        pengguna = Users.objects.all()
        return render(request, 'pages/transaction_trash/create.html', {
            'tempat_sampah': tempat_sampah,
            'pengguna': pengguna,
        })
        
def update(request, id):
    transaction = get_object_or_404(TrashTransaction, id=id)
    if request.method == 'POST':
        tempat_sampah_id = request.POST.get('tempat_sampah')
        berat_sampah = request.POST.get('berat_sampah')
        pengguna_id = request.POST.get('pengguna')

        transaction.tempat_sampah = TrashPlace.objects.get(id=tempat_sampah_id)
        transaction.berat_sampah = berat_sampah
        transaction.pengguna = Users.objects.get(id=pengguna_id)
        transaction.save()
        return redirect('transaction_trash_index')
    else:
        tempat_sampah = TrashPlace.objects.all()
        pengguna = Users.objects.all()
        return render(request, 'pages/transaction_trash/update.html', {
            'transaction': transaction,
            'tempat_sampah': tempat_sampah,
            'pengguna': pengguna,
        })

def delete(request, id):
    transaction = get_object_or_404(TrashTransaction, id=id)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_trash_index')
    return render(request, 'transaction_trash/transaction_confirm_delete.html', {'transaction': transaction})

def process_landfill(request, id):
    return 0