from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
# Create your views here.

def productshow(request):
    l = [0,1,2,3]*10
    return render(request,'product/productBoard.html',{'l':l})