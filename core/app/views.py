from django.shortcuts import render
from .models import *


def main_render(request):
    products = Product.objects.all()
    return render(request, 'app/index.html', {'products': products})


def detail_render(request, pk):
    product = Product.objects.get(id=pk)
    return render(request, 'app/detail.html', {'product': product})
