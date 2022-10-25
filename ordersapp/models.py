from django.db import models
from mainapp.models import Product 
from userapp.models import Profile 
# Create your models here.

class Wishlist(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.product}"