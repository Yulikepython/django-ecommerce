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
    order_item = OrderItem.objects.create(item=item)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        print("qs exists")
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            print("item exists")
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        print("not qs exists")
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
    return redirect("core:product", slug=slug)
