from django.db import models
from django.utils import timezone
from category.models import Category

class TrashPlace(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    address = models.TextField()
    longitude = models.CharField(max_length=255)
    latitude = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'trash_place'

    def __str__(self):
        return f'{self.name} - {self.address}'
