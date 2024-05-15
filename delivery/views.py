from django.shortcuts import render
from customers.models import Customer

# Create your views here.

def home(request):
    return render(request, 'delivery/home.html')

def about(request):
    return render(request, 'delivery/about.html')

def service(request):
    return render(request, 'delivery/service.html')

def blog(request):
    return render(request, 'delivery/blog.html')

def contact(request):
    return render(request, 'delivery/contact.html')

def price(request):
    return render(request, 'delivery/price.html')

def single(request):
    return render(request, 'delivery/single.html')