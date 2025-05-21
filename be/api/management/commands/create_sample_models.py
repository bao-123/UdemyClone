from api.models import User, Product, Order, OrderItem
from django.core.management.base import BaseCommand
from django.utils import lorem_ipsum
from random import randint, sample


class Command(BaseCommand):
    help = "Create sample data for application"

    def handle(self, *args, **kwargs):
        #*Create superuser
        user = User.objects.filter(is_superuser=True).first()
        if not user:
            User.objects.create_superuser(username="admin", password="test")
        
        #*Sample products
        products = [
            Product.objects.create(
                name="Product 1",
                description=lorem_ipsum.paragraph(),
                price=2.99,
                stock=10
            ),
            Product.objects.create(
                name="Product 2",
                description=lorem_ipsum.paragraph(),
                price=5.99,
                stock=100
            ),
            Product.objects.create(
                name="Product 3",
                description=lorem_ipsum.paragraph(),
                price=6.99,
                stock=50
            ),
            Product.objects.create(
                name="Product 4",
                description=lorem_ipsum.paragraph(),
                price=7.77,
                stock=44
            ),
            Product.objects.create(
                name="Product 5",
                description=lorem_ipsum.paragraph(),
                price=3.0,
                stock=777
            ),
            Product.objects.create(
                name="Product 6",
                description=lorem_ipsum.paragraph(),
                price=1.2,
                stock=200
            )
        ]

        #*sample orders (of the superuser)
        for _ in range(5):
            #*Order with 1-6 products
            order = Order.objects.create(user=user)
            for product in sample(products, randint(1, len(products))):
                OrderItem(order=order, product=product, quantity=randint(1, 5))
    