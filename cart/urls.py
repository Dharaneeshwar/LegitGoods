from django.urls import path 
from . import views

urlpatterns=[
    path('',views.mycart,name="mycart"),
    path('payment/',views.payment,name="payment"),
    path('charge/',views.charge,name="charge"),
    path('success/',views.success,name="success"),
    path('getPaymentTemplate/',views.getPaymentTemplate,name = "getPaymentTemplate"),
]
