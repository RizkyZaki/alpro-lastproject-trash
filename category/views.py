from django.shortcuts import render, redirect, get_object_or_404
from .models import Category

def index(request):
    categories = Category.objects.all()
    return render(request, 'pages/category/index.html', {'categories': categories})

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            Category.objects.create(name=name)
            return redirect('category_index')
    return render(request, 'pages/category/create.html')

def update(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            category.name = name
            category.save()
            return redirect('category_index')
    return render(request, 'pages/category/update.html', {'category': category})

def delete(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.delete()
        return redirect('category_index')
    return render(request, 'pages/category/delete.html', {'category': category})
