from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    gender = models.CharField(max_length=10, choices=(('male', 'Male'),('female','Female')))
    city = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True)
    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
