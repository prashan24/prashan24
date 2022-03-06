from django.shortcuts import render
from django.http import HttpResponse

def buy_or_sell(request):
    return render(request, 'buy_or_sell.html')

def contact(request):
    return render(request, 'contact.html')

def dashboard(request):
    return  render(request, 'dashboard.html')

def find_offers(request):
    return  render(request, 'find_offers.html')

    # Create your views here.
