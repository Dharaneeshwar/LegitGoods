from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Product, Category
from .forms import ProductForm
from django.core import serializers

# Create your views here.

def productshow(request):
    categories = Category.objects.all()
    return render(request,'product/productBoard.html',{'categories':categories})

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

def editproduct(request,uid):
    product = Product.objects.get(id = uid)
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
    images = [] 
    temp = {}
    temp['id'] = 0
    temp['image'] = str(product.product_image)
    temp['active'] = 'class="active"'
    temp['active_status'] = 'active'
    images.append(temp)
    if product.product_image2 != 'default.jpg':
        temp = {}
        temp['id'] = 1
        temp['image'] = str(product.product_image2)
        temp['active'] = ''
        temp['active_status'] = ''
        images.append(temp)
    if product.product_image3 != 'default.jpg':
        temp = {}
        temp['id'] = 2
        temp['image'] = str(product.product_image3)
        temp['active_status'] = ''
        temp['active'] = ''
        images.append(temp) 
    print(images)         
    return render(request,'product/productPage.html',{"product":product,'isadded':False,'product_id':product_id,'images':images})     

def categoryprod(request,categoryprod):
    return render(request,'product/filterProducts.html',{'filter':categoryprod,'extendfold':'../','title':'Category : '+categoryprod})       

def allcategory(request):
    return redirect(productshow)   