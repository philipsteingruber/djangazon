from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import *


# Create your views here.
def home(request: HttpRequest) -> HttpResponse:
    items = Item.objects.all()
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.filter(user=request.user).first()
            items_in_cart = cart.items.iterator()
        except AttributeError:
            items_in_cart = []
    else:
        items_in_cart = []
    context = {'items': items, 'items_in_cart': items_in_cart}
    return render(request, 'base/home.html', context=context)


def view_item(request: HttpRequest) -> HttpResponse:
    item = Item.objects.get(id=request.GET['pk'])
    context = {'item': item}
    return render(request, 'base/item.html', context=context)
