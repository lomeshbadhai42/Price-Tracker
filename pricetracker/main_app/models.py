from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.CharField(max_length=1000)
    max_price = models.IntegerField()
    product_name = models.CharField(max_length=255)  # Add this field
    product_price = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    image_url = models.CharField( max_length=555,default="https://media.istockphoto.com/id/155009909/photo/beautiful-smiling-cute-baby.jpg?s=612x612&w=0&k=20&c=-XRwxMdtne8UiFqJC3_k0kW4dsnJXR1tAPxu5dm63lU=")

    def __str__(self):
        return f"Product Details"