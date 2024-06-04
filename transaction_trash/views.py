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
        tempat_sampah_id = request.POST.get('tempat_sampah')
        berat_sampah = request.POST.get('berat_sampah')
        pengguna_id = request.POST.get('pengguna')

        tempat_sampah = TrashPlace.objects.get(id=tempat_sampah_id)
        pengguna = Users.objects.get(id=pengguna_id)

        transaction = TrashTransaction(
            kode_transaksi=kode_transaksi,
            tempat_sampah_id=tempat_sampah_id,
            berat_sampah=berat_sampah,
            pengguna_id=pengguna_id,
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
