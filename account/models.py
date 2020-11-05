from django.db import models
from product.models import Product
# Create your models here.

class User(models.Model):
    phone_number = models.CharField( max_length=12)
    email = models.EmailField(max_length=254)
    userid = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    address = models.TextField()
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        unique_together = [['userid']]


class PurchaseInfo(models.Model):
    seller = models.CharField(max_length=50)
    notification = models.CharField(max_length=120)
    time_created = models.TimeField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    deliver_to = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.notification+str(self.quantity)


        
