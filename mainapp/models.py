from django.db import models

# Create your models here.

class MainSection(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='mainsections', blank=True, null=True)  # creates 'mainsections' folder in media folder and stores there
    def __str__(self) -> str : return self.name

class Section(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='sections', blank=True, null=True)  # creates 'sections' folder in media folder and stores there
    mainsection = models.ForeignKey(MainSection, on_delete=models.CASCADE, null=True)
    def __str__(self) -> str : return self.name

class Inner(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField(upload_to='inner_sections', blank=True, null=True)  # creates 'inner_sections' folder in media folder and stores there
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name="inners")
    def __str__(self) -> str : return self.name

class Product(models.Model):
    name = models.CharField(max_length=70)
    brand = models.CharField(max_length=70)
    details = models.CharField(max_length=70)
    guarantee = models.CharField(max_length=70)
    shipping = models.CharField(max_length=70)
    price = models.PositiveSmallIntegerField()
    discount = models.PositiveSmallIntegerField(default=0)
    instock = models.PositiveSmallIntegerField()
    min_order = models.CharField(max_length=30, default="")
    inner = models.ForeignKey(Inner, on_delete=models.SET_NULL, null=True, related_name="products")
    def __str__(self) -> str:
        return self.name

class Image(models.Model):
    image = models.FileField(upload_to='products')
    product = models.ForeignKey(Product, on_delete=models.CASCADE , related_name="images")
    def __str__(self) -> str:
        return f'{self.product}'