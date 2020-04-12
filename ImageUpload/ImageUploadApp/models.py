from django.db import models

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=300)
    content=models.CharField(max_length=1000)
    image=models.ImageField()
