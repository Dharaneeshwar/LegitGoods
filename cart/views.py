from django.shortcuts import render

# Create your views here.

def mycart(request):
    return render(request,'cart/cart.html')

def payment(request):
    return render(request,'cart/payment_base.html')    