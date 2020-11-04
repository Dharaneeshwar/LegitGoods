from django.urls import path 
from . import views

urlpatterns=[
    path('',views.mycart,name="mycart"),
    path('payment/',views.payment,name="payment"),
]
