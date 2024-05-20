from django.shortcuts import render
from .models import Customer

def index(request):
    customers = Customer.objects.all() 
    return render(request, 'index.html', {'data': customers}) 
