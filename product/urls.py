from django.urls import path 
from . import views

urlpatterns=[
    path('',views.productshow,name="productshow"),
    path('addproduct/',views.addProduct,name="addproduct"),
    path('myproducts/',views.myproducts,name="myproducts"),
    path('editproduct/<str:uid>/',views.editproduct,name="myproducts"),
    path('product/<str:slim>/',views.productPage, name="productpage")
]
