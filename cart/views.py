from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
from .models import Cart
from product.models import Product
from account.models import User
from .stripe_cred import api_key
import stripe
# Create your views here.

stripe.api_key = api_key

def mycart(request):
    return render(request,'cart/cart.html')

def payment(request):
    return render(request,'cart/payment_base.html')    


def getPaymentTemplate(request):
    if request.method == 'POST':
        uid = request.POST['uid']
        user = User.objects.get(userid = uid)
        
        if str(user.country).lower() == "india":
            isIndian = True
        else:
            isIndian = False    
        print('uid : ',uid)
        subtotal = 0
        total = 0
        deliveryCharge = 0
        all_cart_products = Cart.objects.filter(userid = uid).order_by('id')   
        print(all_cart_products)
        products = []
        for cart_ele in all_cart_products:
            product = cart_ele.product
            temp = {} 
            temp ['id'] = product.pk
            temp ['title'] = product.title 
            temp ['price'] = "₹"+str(int(product.selling_price)) 
            temp ['quantity'] = cart_ele.quantity
            temp ['amount'] = "₹"+str(int(cart_ele.quantity * product.selling_price))
            products.append(temp)
            subtotal += int(temp['amount'][1:])
        print(products)    
        if isIndian:
            deliveryCharge = 100
        else:
            deliveryCharge = 1000
        total += subtotal+deliveryCharge
        return render(request,'cart/payment.html',{'products':products,'subtotal':subtotal,'total':total,'deliveryCharge':deliveryCharge})
    else:
        return JsonResponse({"status":"Get Not supported"})       


def charge(request):
    subtotal = 0
    total = 0
    deliveryCharge = 0
    if request.method == "POST":
        print("data : ",request.POST)
        uid = request.POST['uid']
        all_cart_products = Cart.objects.filter(userid = uid)
        user = User.objects.get(userid = uid)
        if str(user.country).lower() == "india":
            isIndian = True
        else:
            isIndian = False  
        for cart_ele in all_cart_products:
            product = cart_ele.product
            temp = {} 
            temp ['amount'] = "₹"+str(int(cart_ele.quantity * product.selling_price))
            subtotal += int(temp['amount'][1:])
        user = User.objects.get(userid = uid)
        if isIndian:
            deliveryCharge = 100
        else:
            deliveryCharge = 1000
        total += subtotal+deliveryCharge
        # customer = stripe.Customer.create(
        #     name = user.name,
        #     email = user.email,
        #     source = request.POST['stripeToken']
        # )        
        meta = {
            'name' : user.name,
            'email' : user.email,
            'charge' : total             
        }
        charge = stripe.Charge.create(
            amount=total*100,
            currency="inr",
            source=request.POST['stripeToken'],
            description="Payment Bill",
            metadata = meta
        )
    return redirect('../success/')    

def success(request):
    return render(request,'cart/success.html')    