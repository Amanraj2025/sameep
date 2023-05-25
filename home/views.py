from django.shortcuts import render
from django.http import HttpResponse
from .models import product
from math import ceil

# Create your views here.
def index(request):
    products = product.objects.all()
    print(products)
    n = len(products)
    nSlides = n//4+ceil(n/4-n//4)
    params = {'num_slides': nSlides, 'range': range(1, nSlides), 'product': products}
   
    return render(request, 'index.html', params)


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def tracker(request):
    return render(request, 'tracker.html')


def productview(request):
    return render(request, 'productview.html')


def search(request):
    return render(request, 'search.html')


def checkout(request):
    return render(request, 'checkout.html')


def wishlist(request):
    return HttpResponse('Wishlist')
