from django.shortcuts import render, redirect
from .models import Category
from .forms import CategoryForm

def index(request):
    categories = Category.objects.all()
    return render(request, 'pages/category/index.html', {'categories': categories})

def create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('category_index')
    else:
        form = CategoryForm()
    return render(request, 'pages/category/create.html', {'form': form})
