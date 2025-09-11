from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):

    def setUp(self):
        Product.objects.create(name="Laptop", price=1200, description="A fast laptop")
        Product.objects.create(name="Phone", price=800, description="Latest smartphone")

    def test_product_count(self):
        products = Product.objects.all()
        self.assertEqual(products.count(), 2)

    def test_product_name(self):
        laptop = Product.objects.get(name="Laptop")
        self.assertEqual(laptop.description, "A fast laptop")
