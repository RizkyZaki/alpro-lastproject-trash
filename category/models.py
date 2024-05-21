from django.db import models
from django.utils import timezone

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        db_table = 'category'
    def __str__(self):
        return f'{self.name}'
