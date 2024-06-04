import os
import django
from django.conf import settings
from django.contrib.auth.hashers import make_password

# Atur lingkungan Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tubes_sampah.settings')
django.setup()

from users.models import Users

def create_super_admin():
    # Cek apakah pengguna super admin sudah ada dalam database
    if not Users.objects.filter(role='superadmin').exists():
        # Jika tidak ada, tambahkan entri pengguna super admin
        super_admin = Users.objects.create(
            name='Super Admin',
            email='super@gmail.com',
            password=make_password('Default'),  # Meng-hash password
            role='superadmin'
        )
        print('Super admin berhasil ditambahkan:', super_admin)
    else:
        print('Pengguna super admin sudah ada dalam database.')

if __name__ == '__main__':
    create_super_admin()
