from django.db import models
from django.contrib.auth.hashers import check_password as check_password_hash


class EnumField(models.CharField):
    def db_type(self, connection):
        return 'ENUM'

class Users(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    role = EnumField(max_length=255, choices=[('superadmin', 'Super Admin'), ('admin', 'Admin')], default='admin')
    last_login = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return f'{self.name}'

