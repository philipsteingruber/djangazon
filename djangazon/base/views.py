from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
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


def add_to_cart(request: HttpRequest, pk) -> HttpResponse:
    item = Item.objects.get(id=pk)
    cart = Cart.objects.filter(user=request.user).first()
    try:
        cartitem = CartItem.objects.get(cart=cart, item=item)
        cartitem.quantity += 1
    except CartItem.DoesNotExist:
        cartitem = CartItem.objects.create(cart=cart, item=item, quantity=1)
        cartitem.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
