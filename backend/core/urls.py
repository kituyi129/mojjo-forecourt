from django.urls import path
from .views import products, products_details

urlpatterns = [
    path("", products, name ="product_list"),
    path("product/<slug:slug>/", products_details, name="product_details"),
   
]
