from django.urls import path, include 
from . import views
urlpatterns=[
    path('allproduct/',views.allProducts,name = "allprod"),
    path('myproducts/<str:uid>/',views.myProducts,name = "myprod"),
    path('getCartinfo/',views.getCartinfo,name = "getCartinfo"),
    path('addToCart/',views.addToCart,name = "addToCart"),
    path('removeFromCart/',views.removeFromCart,name = "removeFromCart"),
    path('updateQuantity/',views.updateQuantity,name = "updateQuantity"),
    path('getCartProdcuts/',views.getCartProdcuts,name = "getCartProdcuts"),
    path('filterproduct/',views.filterproduct,name = "filterproduct"),
    path('clearCart/',views.clearCart,name = "clearCart"),
    path('productsToDeliver/',views.productsToDeliver,name = "productsToDeliver"),
]