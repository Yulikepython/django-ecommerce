from django.urls import path

from .views import HomeView, ProductView, add_to_cart

app_name="core"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("product/<slug:slug>/", ProductView.as_view(), name="product"),
    path('add-to-cart/<slug:slug>/', add_to_cart, name="add-to-cart"),
]