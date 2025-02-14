from django.db import models
from steamShop.settings import AUTH_USER_MODEL

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(max_length=128)
    price = models.FloatField(default=0.0)
    description = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to="products",blank=True,null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return f"/product/{self.slug}"
    
class Order(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quanntity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
     
    def __str__(self):
        return f"{self.quanntity} of {self.product.name} by {self.user.username}" 
    

class Cart(models.Model):
    user =models.OneToOneField(AUTH_USER_MODEL,on_delete=models.CASCADE)
    order = models.ManyToManyField(Order)
    ordered = models.BooleanField(default=False)
    ordered_date = models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return f"{self.user.username} cart"