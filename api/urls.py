from django.urls import path, include 
from . import views
urlpatterns=[
    path('allproduct/',views.allProducts,name = "allprod"),
    path('myproducts/<str:uid>/',views.myProducts,name = "myprod"),
]