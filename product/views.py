from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'product': products})
    return render(request, 'index.html', {''})


def new(request):
    return HttpResponse('new product')




# Create your views here.
