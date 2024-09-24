from django.db import models
from django.contrib.auth.models import User

import uuid

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False) 
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    stock = models.IntegerField(default=0)
    category = models.CharField(max_length=100)
    rating = models.FloatField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    review = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
