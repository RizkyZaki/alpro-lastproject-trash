from django.db import models
from django.utils import timezone

class TrashPlace(models.Model):
    id = models.AutoField(primary_key=True)
    id_category = models.IntegerField(max_length=20)
    name = models.CharField(max_length=255)
    address = models.TextField()
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'trash_place'
    def __str__(self):
        return f'{self.id_category},{self.name},{self.address}, {self.longitude}, {self.latitude}'
