"""

Kelas = SI4706
Kelompok = 11
Anggota Kelompok
1. Rizky Zaki Zulkarnaen 102022300080
https://zach-me.vercel.app

"""
from django.shortcuts import render
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from users.models import Users
from trash_place.models import TrashPlace
from tps.models import Tps
from tpa.models import  Tpa
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from datetime import datetime
from category.models import Category
import calendar
from django.db.models import Count, Sum, Q
from django.db.models.functions import TruncMonth

def index(request):
    # Data for Trash Places
    trash_places = TrashPlace.objects.all()
    places = [
        {
            'name': place.name,
            'latitude': place.latitude,
            'longitude': place.longitude,
        } for place in trash_places
    ]

    transactions = Tps.objects \
        .annotate(month=TruncMonth('tanggal')) \
        .values('month') \
        .annotate(total_weight=Sum('berat_sampah')) \
        .order_by('month')

    chart_labels = [calendar.month_name[transaction['month'].month] for transaction in transactions]
    chart_data = {
        'labels': chart_labels,
        'data': [float(transaction['total_weight']) if transaction['total_weight'] else 0 for transaction in transactions],  # Ensure it's float
    }

    category_data = TrashPlace.objects.values('category__name').annotate(total_places=Count('id'))
    pie_chart_data = {
        'labels': [data['category__name'] for data in category_data],
        'data': [data['total_places'] for data in category_data],
    }

    # Additional counts and sums
    total_places = TrashPlace.objects.count()
    total_landfills = Tpa.objects.count()
    total_users = Users.objects.count()
    total_weight = Tps.objects.aggregate(Sum('berat_sampah'))['berat_sampah__sum']

    return render(request, 'pages/dashboard.html', {
        'places': json.dumps(places),
        'chart_data': json.dumps(chart_data),
        'pie_chart_data': json.dumps(pie_chart_data),
        'total_places': total_places,
        'total_landfills': total_landfills,
        'total_users': total_users,
        'total_weight': total_weight,
    })
    
def search(request):
    query = request.GET.get('q')
    if query:
        results = TrashPlace.objects.filter(
            Q(name__icontains=query) |
            Q(category__name__icontains=query) |
            Q(latitude__icontains=query) |
            Q(longitude__icontains=query)
        )
    else:
        results = TrashPlace.objects.all()
    
    return render(request, 'pages/trash_place/index.html', {'trash_places': results, 'query': query})

def filter(request):
    month = request.GET.get('month')
    tps = Tps.objects.select_related('trash_place', 'tpa').all()
    tps = tps.filter(tanggal__month=month)
    return render(request, 'pages/tps/index.html', {'tps': tps})

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
