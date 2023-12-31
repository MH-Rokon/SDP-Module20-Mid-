
from django.db import models
from django.contrib.auth.models import User
from categories.models import Brand

class Car(models.Model):
    brands = models.ManyToManyField(Brand)
    name = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='upload/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"{self.brands}  {self.name}"
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_cars = models.ManyToManyField(Car)

    def __str__(self):
        return self.user.username