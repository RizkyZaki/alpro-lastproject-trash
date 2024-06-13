"""

Kelas = SI4706
Kelompok = 11
Anggota Kelompok
1. Rizky Zaki Zulkarnaen 102022300080
https://zach-me.vercel.app

"""
from django.db import models
from users.models import Users
from trash_place.models import TrashPlace  # Sesuaikan dengan nama app dan model
from tpa.models import Tpa  # Sesuaikan dengan nama app dan model

class Tps(models.Model):
    kode_transaksi = models.CharField(max_length=50, unique=True)
    trash_place = models.ForeignKey(TrashPlace, on_delete=models.CASCADE, db_column='trash_place_id')
    berat_sampah = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, db_column='user_id')
    tpa = models.ForeignKey(Tpa, on_delete=models.SET_NULL, null=True, db_column='tpa_id')
    tanggal = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tps'

    def __str__(self):
        return self.kode_transaksi
