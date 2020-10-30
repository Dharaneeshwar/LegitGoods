from django.shortcuts import render
from django.http import JsonResponse
from product.models import Product, Tag, Category
from django.core import serializers

def allProducts(request):
    all_prod = Product.objects.filter(isActive = True)
    all_prod = serializers.serialize('json',all_prod)
    return JsonResponse(all_prod,safe = False)

def myProducts(request,uid):
    all_prod = Product.objects.filter(userid = uid)
    all_prod = serializers.serialize('json',all_prod)
    return JsonResponse(all_prod,safe = False)
