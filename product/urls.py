from django.urls import path 
from . import views

urlpatterns=[
    path('',views.productshow,name="productshow"),
    path('addproduct/',views.addProduct,name="addproduct"),
    path('myproducts/',views.myproducts,name="myproducts"),
    path('productsToDeliver/',views.productsToDeliver,name="productsToDeliver"),
    path('editproduct/<str:uid>/',views.editproduct,name="myproducts"),
    path('product/<str:slim>/',views.productPage, name="productpage"),
    path('category/<str:categoryprod>/',views.categoryprod, name="categoryprod"),
    path('category/',views.allcategory, name="allcategory")
]
