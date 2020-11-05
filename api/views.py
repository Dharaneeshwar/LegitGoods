from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from product.models import Product, Category 
from cart.models import Cart
from account.models import PurchaseInfo, User
from django.core import serializers
import os
from .twilio import account_sid,auth_token
from twilio.rest import Client

client = Client(account_sid, auth_token)

def allProducts(request):
    all_prod = Product.objects.filter(isActive = True)
    all_prod = serializers.serialize('json',all_prod)
    return JsonResponse(all_prod,safe = False)

def myProducts(request,uid):
    all_prod = Product.objects.filter(userid = uid)
    all_prod = serializers.serialize('json',all_prod)
    return JsonResponse(all_prod,safe = False)

def getCartinfo(request):
    uid = request.GET['uid']
    product_id = request.GET['product_id']
    product = Product.objects.get(id = product_id)
    if Cart.objects.filter(product = product,userid = uid).exists():
        cart = Cart.objects.filter(product = product,userid = uid)
        data = {
            'status':True,
            'cart':serializers.serialize('json',cart),
            'product_available':product.inStock,
            'max_number':product.quantity
        }
        print(cart)
    else:
        data = {
            'status':False,
            'cart':'{}',
            'max_number':product.quantity,
            'product_available':product.inStock
        } 
    return JsonResponse({'data':data})

def addToCart(request):
    uid = request.GET['uid']
    product_id = request.GET['product_id']
    quantity = request.GET['quantity']
    product = Product.objects.get(pk = product_id)
    cart = Cart(product = product,userid = uid,quantity = quantity)
    cart.save()
    return JsonResponse({'message':'successfully added to cart'})

def removeFromCart(request):
    uid = request.GET['uid']
    product_id = request.GET['product_id']
    product = Product.objects.get(pk = product_id)
    cart = Cart.objects.filter(product = product,userid = uid)[0]
    cart.delete()
    return JsonResponse({'message':'successfully deleted'})
    
def updateQuantity(request):
    uid = request.GET['uid']
    product_id = request.GET['product_id']
    quantity = request.GET['quantity']
    product = Product.objects.get(id = product_id)
    if Cart.objects.filter(product = product,userid = uid).exists():
        cart = Cart.objects.filter(product = product,userid = uid)[0]
        if int(quantity)==0:
            print("delete")
            cart.delete()
            data = {
                'status':"Deleted",
            }
        else:   
            print("not deleted")
            cart.quantity = quantity
            cart.save()
            data = {
                'status':"Updated",
            }
        print(cart)
    else:

        data = {
            'status':"Product is not in the cart",
        } 
    return JsonResponse({'data':data})

def getCartProdcuts(request):
    uid = request.GET['uid']
    all_cart_products = Cart.objects.filter(userid = uid).order_by('id')   
    print(all_cart_products)
    products = []
    for cart_ele in all_cart_products:
        product = cart_ele.product
        temp = {} 
        temp ['id'] = product.pk
        temp ['title'] = product.title 
        temp ['subtitle'] = product.subtitle 
        temp ['price'] = product.selling_price 
        temp ['quantity'] = cart_ele.quantity
        temp ['image'] = str(product.product_image)
        products.append(temp)
    return JsonResponse(products,safe = False)    

def filterproduct(request):
    filter_category = request.GET['type']
    category = Category.objects.get(category = filter_category)
    filter_prod = Product.objects.filter(isActive = True,category = category)
    filter_prod = serializers.serialize('json',filter_prod)
    return JsonResponse(filter_prod,safe = False)

def clearCart(request):
    uid = request.GET['uid']
    user_purchased = User.objects.get(userid = uid)
    all_cart_products = Cart.objects.filter(userid = uid).order_by('id')
    for cart in all_cart_products:
        product = cart.product
        seller = User.objects.get(userid = product.userid)
        client.messages.create(from_='+19387772555',
                       to='+91'+seller.phone_number,
                       body=f"Congratulations! {cart.quantity} items of your product '{product.title}' sold on LegitGoods! Check it out on the Website.")
        # print(f"Congratulations! Your product '{product.title}' sold on LegitGoods! Check it out on the Website.")
        purchase = PurchaseInfo(product = product,seller = product.userid,notification = f"{product.title} Purchased!",quantity = cart.quantity,amount = product.selling_price*cart.quantity,deliver_to = user_purchased)
        purchase.save()
    all_cart_products.delete()
    return JsonResponse({'message':'Cart Cleared!'})    

def productsToDeliver(request):
    uid = request.GET['uid']
    all_prod_purchased = PurchaseInfo.objects.filter(seller = uid)
    products = []
    for prod in all_prod_purchased:
        prod_info = {} 
        prod_info['notification'] = prod.notification
        prod_info['time'] = prod.time_created
        product_obj = prod.product
        prod_info['prod_title'] = product_obj.title 
        prod_info['quantity'] = prod.quantity 
        prod_info['amount'] = prod.amount 
        user = prod.deliver_to 
        prod_info['user_name'] = user.name 
        prod_info['user_email'] = user.email 
        prod_info['user_address'] = user.address
        prod_info['user_country'] = user.country
        prod_info['user_state'] = user.state
        prod_info['user_pin'] = user.pincode
        products.append(prod_info)        
    return JsonResponse(products,safe = False)