from django.db import models

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
    
    