from django.shortcuts import render, redirect
from .models import User
from django.http import JsonResponse
from .forms import UserForm
# Create your views here.

def login(request):
    return render(request,'accounts/login.html')

def profile(request,uid):
    if request.method == "POST":
        if User.objects.filter(userid = uid).exists():
            inst = User.objects.get(userid = uid)
            form = UserForm(request.POST, instance = inst)
        else:
            form = UserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print("yes")
            return redirect('../../../')
        else:
            print("no no")   
    else:
        if User.objects.filter(userid = uid).exists():
            inst = User.objects.get(userid = uid)
            form = UserForm(instance = inst)
        else:
            form = UserForm()     
    print("no")
    return render(request,'accounts/profile.html',{'form':form.as_p()})    

def notification(request):
    return render(request,'accounts/profile.html')

def payout(request):
    return render(request,'accounts/payout.html')    


