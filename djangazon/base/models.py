from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(blank=False, null=False)
    category = models.ManyToManyField('Category', blank=False)
    description = models.TextField(blank=True)
    image = models.ImageField(default='images/imagenotfound.jpg', blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    items = models.ManyToManyField(Item)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    items = models.ManyToManyField(Item)
