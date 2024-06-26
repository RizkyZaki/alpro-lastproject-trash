"""

Kelas = SI4706
Kelompok = 11
Anggota Kelompok
1. Rizky Zaki Zulkarnaen 102022300080
https://zach-me.vercel.app

"""
from django.db import models

class Tpa(models.Model):
    nama = models.CharField(max_length=255)
    alamat = models.TextField()
    keterangan = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'tpa'
        
    def __str__(self):
        return self.nama
