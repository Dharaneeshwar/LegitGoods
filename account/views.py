from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.

def login(request):
    return render(request,'accounts/login.html')