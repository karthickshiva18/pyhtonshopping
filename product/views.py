from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('hello world')


def new(request):
    return HttpResponse('new product')




# Create your views here.