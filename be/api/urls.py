from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.product_list),
    path("products/<int:pk>", views.product_info, name="product_info"),
    path("orders/", views.order_list)
    #path("orders/<int:user_id>", views.order_list)
]