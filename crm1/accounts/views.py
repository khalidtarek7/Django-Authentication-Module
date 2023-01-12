from django.shortcuts import render
from django.http import HttpResponse
from .models import login

# Create your views here.
def home(request):
    return render(request,'accounts/dashboard.html')

def products(request):
    return render(request,'accounts/products.html')

def customer(request):
    username = request.POST.get('username')
    password =  request.POST.get('password')
    data = login(username=username, password=password)
    data.save()
    return render(request,'accounts/customer.html')