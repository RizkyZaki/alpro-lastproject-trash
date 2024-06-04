from django.db import models

class Landfill(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.TextField()
    keterangan = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'landfill'
    def __str__(self):
        return self.nama
