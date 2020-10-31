from django.db import models
from product.models import Product
# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    userid = models.CharField(max_length=50)
    quantity = models.IntegerField(default = 1)

    def __str__(self):
        return str(self.quantity)

    class Meta:
        unique_together = [['product','userid']]    