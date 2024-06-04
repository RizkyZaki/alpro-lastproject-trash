"""

Kelas = SI4706
Kelompok = 11
Anggota Kelompok
1. Rizky Zaki Zulkarnaen 102022300080
https://zach-me.vercel.app

"""
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from users.models import Users


def index(request):
    return render(request, 'pages/dashboard.html') 

def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate_user(email, password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect ke halaman yang diinginkan setelah login
        else:
            messages.error(request, 'Email atau password salah.')
    return render(request, 'pages/auth/login.html')

from django.contrib.auth.hashers import check_password

def authenticate_user(email, password):
    try:
        user = Users.objects.get(email=email)
        if check_password(password, user.password):
            return user
    except Users.DoesNotExist:
        return None


@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
