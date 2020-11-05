from django.contrib import admin
from .models import User, PurchaseInfo, RequestPayout
# Register your models here.

admin.site.register(User)
admin.site.register(PurchaseInfo)
admin.site.register(RequestPayout)