from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100, unique=True)
    price = models.FloatField(blank=False, null=False)
    category = models.ManyToManyField('Category', blank=False)
    description = models.TextField(blank=True)
    image = models.ImageField(default='assets/imagenotfound.jpg', blank=True)
    slug = models.SlugField(max_length=100, unique=True, default=slugify(name), editable=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created = models.DateTimeField(auto_now_add=True)
    delivered = models.BooleanField(default=False)
    delivered_date = models.DateField(blank=True, null=True)
    items = models.ManyToManyField('CartItem')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} x {self.item}'
