from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

from django.views.generic import ListView, TemplateView, DetailView
from django.utils import timezone
from .models import Item, OrderItem, Order

class HomeView(ListView):
    template_name="home-page.html"
    model = Item

class ProductView(DetailView):
    template_name="product-page.html"
    model = Item

class CheckOutView(TemplateView):
    template_name="checkout-page.html"

def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(item=item,user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "items quantity was updated.")
        else:
            messages.info(request, "items was added to your cart")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "items was added to your cart")
    return redirect("core:product", slug=slug)


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(item=item,user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "This items was remove from your cart")
        else:
            messages.info(request, "This items was not in your cart")
            return redirect("core:product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:product", slug=slug)

    return redirect("core:product", slug=slug)