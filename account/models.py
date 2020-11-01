from django.db import models

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