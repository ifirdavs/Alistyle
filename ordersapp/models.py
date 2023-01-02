from django.db import models
from django.core.exceptions import ValidationError
from mainapp.models import Product 
from userapp.models import Profile 
# Create your models here.

def validate_amount(value):
    if value >= 1 and value <=10:
        return value
    else:
        raise ValidationError("Min is 1, max is 10")


class Wishlist(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.product}"

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    amount = models.PositiveSmallIntegerField(default=1, validators=[validate_amount])
    total = models.PositiveIntegerField()
    def __str__(self) -> str:
        return f"{self.product.name}"

class Order(models.Model):
    cart = models.ManyToManyField(CartItem)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    items_total = models.PositiveSmallIntegerField()
    shipping_fee = models.PositiveSmallIntegerField(default=5)
    total = models.PositiveSmallIntegerField()
    def __str__(self) -> str:
        return f"{self.profile}"