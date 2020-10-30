from django.db import models

# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.tag

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Product(models.Model):
    title = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    stars = models.FloatField(default=0.0)
    desc = models.TextField(max_length=500, blank=True)
    num_rating = models.IntegerField(default=0)
    marked_price = models.FloatField()
    selling_price = models.FloatField()
    tags = models.ManyToManyField(Tag , blank = True)
    product_image = models.ImageField(blank= True,upload_to='./',default = 'default.jpg')
    product_image2 = models.ImageField(blank= True, upload_to='media',default = 'default.jpg')
    product_image3 = models.ImageField(blank= True, upload_to='media',default = 'default.jpg')
    created_time = models.DateTimeField(auto_now=True, auto_now_add=False)
    offer_present = models.BooleanField(default = False)
    userid = models.CharField(max_length=50) 
    category = models.ManyToManyField(Category, blank = True)
    isActive = models.BooleanField(default = True)
    quantity = models.IntegerField(default=1)
    inStock = models.BooleanField(default = True)

    def __str__(self):
        return self.title