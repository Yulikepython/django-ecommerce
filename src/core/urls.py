from django.urls import path

from .views import (HomeView, 
                    ProductView, 
                    add_to_cart, 
                    remove_from_cart,
                    OrderSummaryView,
                    CheckOutView,
                    remove_single_item_from_cart
                    )

app_name="core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<slug:slug>/", ProductView.as_view(), name="product"),
    path("order-summary/", OrderSummaryView.as_view(), name="order-summary"),
    path('add-to-cart/<slug:slug>/', add_to_cart, name="add-to-cart"),
    path('remove-from-cart/<slug:slug>/', remove_from_cart, name="remove-from-cart"),
    path("checkout/", CheckOutView.as_view(), name="checkout"),
    path('remove-item-from-cart/<slug:slug>/', remove_single_item_from_cart, name="remove-single-item-from-cart"),

]