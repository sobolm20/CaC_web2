from django.db import models

# Create your models here.
class food(models.Model):
    title = models.CharField(max_length=200)
    ingredients = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=3)
    image = models.ImageField(upload_to="dishes")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
