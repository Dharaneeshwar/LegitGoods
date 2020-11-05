from django.urls import path 
from . import views

urlpatterns=[
    path('login/',views.login,name="login"),
    path('profile/<str:uid>/',views.profile,name="profile"),
    path('notification/',views.notification,name="notification"),
]
