from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product 
from .forms import ProductForm
from django.core import serializers

# Create your views here.

def productshow(request):
    return render(request,'product/productBoard.html')

def addProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            # product_new = Product(title = data['title'],subtitle=data['subtitle'],desc = data['desc'],marked_price = data['marked_price'],selling_price = data['selling_price'],product_image = data['product_image'],offer_present = data['offer_present'],userid = data['userid'])
            # product_new.save()
            # form = ProductForm(request.POST, request.FILES)
            form.save()
            print("yes")
            return redirect('../')
        else:
            print("no no")   
    else:
        form = ProductForm()     
    print("no")    
    return render(request,'product/addproduct.html',{'form':form.as_p()})    

def myproducts(request):
    return render(request,'product/myProducts.html')

def editproduct(request,id):
    product = Product.objects.get(id = id)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES,instance = product)
        if form.is_valid():
            data = form.cleaned_data
            # product_new = Product(title = data['title'],subtitle=data['subtitle'],desc = data['desc'],marked_price = data['marked_price'],selling_price = data['selling_price'],product_image = data['product_image'],offer_present = data['offer_present'],userid = data['userid'])
            # product_new.save()
            # form = ProductForm(request.POST, request.FILES)
            form.save()
            print("yes")
            return redirect('../../myproducts')
        else:
            print("no no")   
    else:
        form = ProductForm(instance = product)     
    return render(request,'product/editProduct.html',{'form':form.as_p()})


def productPage(request,slim):
    product_id = slim.split('-')[0]
    product = Product.objects.get(id = product_id)
    return render(request,'product/productPage.html',{"product":product,'isadded':False})     