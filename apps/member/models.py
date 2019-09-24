from django.db import models

# Create your models here.
class Members(models.Model):
    name        = models.CharField(max_length=120)
    position    = models.CharField(max_length=120)
    age         = models.CharField(max_length=20)
    gender      = models.CharField(max_length=64)
    phone       = models.CharField(max_length=12)
    address     = models.CharField(max_length=120)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)
