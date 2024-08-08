from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .models import *


def home(request: HttpRequest, action: str = 'items') -> HttpResponse:
    items = Item.objects.all().order_by('name')
    categories = Category.objects.all().order_by('name')

    if request.user.is_authenticated:
        try:
            cart = Cart.objects.filter(user=request.user).first()
            items_in_cart = cart.items.iterator()
        except Cart.DoesNotExist:
            items_in_cart = []
            cart = Cart.objects.create(user=request.user)
            cart.save()
    else:
        items_in_cart = []
        cart = None
    context = {'items': items, 'items_in_cart': items_in_cart, 'categories': categories, 'cart': cart, 'action': action}
    return render(request, 'base/home.html', context=context)


def view_item(request: HttpRequest, pk: str) -> HttpResponse:
    item = Item.objects.get(slug=pk)
    context = {'item': item}
    return render(request, 'base/item.html', context=context)


@login_required
def add_to_cart(request: HttpRequest, pk) -> HttpResponse:
    item = Item.objects.get(id=pk)
    cart = Cart.objects.filter(user=request.user).first()
    try:
        cartitem = CartItem.objects.get(cart=cart, item=item)
        cartitem.quantity += 1
    except CartItem.DoesNotExist:
        cartitem = CartItem.objects.create(cart=cart, item=item, quantity=1)
        cartitem.save()

    return redirect('view_item', pk=pk)


def buy_item(request, pk: str) -> HttpResponse:
    item = Item.objects.get(id=pk)
    user = request.user

    try:
        Cart.objects.filter(user=user).first()
    except Cart.DoesNotExist:
        new_cart = Cart.objects.create(user=user)
        new_cart.save()

    cart = Cart.objects.filter(user=user).first()
    try:
        cartitem = CartItem.objects.get(cart=cart, item=item)
        cartitem.quantity += 1
        cartitem.save()
    except CartItem.DoesNotExist:
        cartitem = CartItem.objects.create(cart=cart, item=item, quantity=1)
        cartitem.save()
    return redirect('home')


def sign_out(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def delete_item_from_cart(request, pk, amount):
    item = Item.objects.get(id=pk)
    cart = Cart.objects.get(user=request.user)
    cartitem = CartItem.objects.get(item=item, cart=cart)

    if amount.isdecimal():
        amount = int(amount)
        cartitem.quantity -= amount
        if cartitem.quantity <= 0:
            cartitem.delete()
        else:
            cartitem.save()
    else:
        if amount == 'all':
            cartitem.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def user_profile(request, pk):
    context = {'user': request.user}
    return render(request, 'base/home.html', context=context)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').casefold()
        password = request.POST.get('password')

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return home(request, action='login')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return home(request, action='login')
    else:
        return home(request, action='login')
