from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.ProductListAPIView.as_view()),
    path("products/<int:pk>", views.ProductDetailAPIView.as_view(), name="product_info"),
    path("orders/", views.OrderListAPIView.as_view()),
    path("orders/user", views.UserOrderListAPIView.as_view())
    #path("orders/<int:user_id>", views.order_list)
]