from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from . models import Product


def index(request):
    products = Product.objects.all()

    return render(request, 'index.html', {'products': products})


def new(req):
    return render(req, 'new.html')


