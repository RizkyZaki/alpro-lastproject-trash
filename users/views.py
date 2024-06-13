"""

Kelas = SI4706
Kelompok = 11
Anggota Kelompok
1. Rizky Zaki Zulkarnaen 102022300080
https://zach-me.vercel.app

"""
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password 
from .models import Users

def index(request):
    users = Users.objects.all()
    return render(request, 'pages/user/index.html', {'users': users})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = make_password(request.POST.get('password'))  # Meng-hash password
        role = 'admin'

        Users.objects.create(name=name, email=email, password=password, role=role)
        return redirect('user_index')
    return render(request, 'pages/user/create.html')

def update(request, id):
    user = Users.objects.get(id=id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.password = request.POST.get('password')
        user.role = 'admin'
        user.save()
        return redirect('user_index')
    return render(request, 'pages/user/update.html', {'user': user})

def delete(request, id):
    user = Users.objects.get(id=id)
    if request.method == 'POST':
        user.delete()
        return redirect('user_index')
    return render(request, 'pages/user/delete.html', {'user': user})

def reset_password(request, id):
    user = Users.objects.get(id=id)
    user.password = make_password('Default')  
    user.save()
    return redirect('user_index')
  

  
  

