from django.db import models
from users.models import Users
from trash_place.models import TrashPlace  # Sesuaikan dengan nama app dan model
from landfill.models import Landfill  # Sesuaikan dengan nama app dan model

class TrashTransaction(models.Model):
    kode_transaksi = models.CharField(max_length=50, unique=True)
    tempat_sampah_id = models.ForeignKey(TrashPlace, on_delete=models.CASCADE)
    berat_sampah = models.DecimalField(max_digits=10, decimal_places=2)
    pengguna_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    tujuan_id = models.ForeignKey(Landfill, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'trash_transaction'

    def __str__(self):
        return self.kode_transaksi
