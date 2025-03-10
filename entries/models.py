from django.db import models

# Create your models here.
class Entrie(models.Model):
    title=models.CharField(max_length=100)
    compound=models.CharField(max_length=300)
    cooking=models.CharField(max_length=800)
    