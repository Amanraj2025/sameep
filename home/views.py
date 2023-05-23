from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    #return HttpResponse('This is home page')
    return render(request, 'SoftLand/aman-index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def tracker(request):
    return render(request, 'tracker.html')

def productView(request):
    return render(request, 'productView.html')

def search(request):
    return render(request, 'search.html')

def checkout(request):
    return render(request, 'checkout.html')

def wishlist(request):
    return HttpResponse('Wishlist')




