from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Product

class ProductTestCase(APITestCase):
    def test_create_product(self):
        url = reverse('product-list')
        data = {'name': 'Laptop', 'price': 1200.00, 'description': 'High performance laptop'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'Laptop')

    def test_get_product(self):
        product = Product.objects.create(name='Laptop', price=1200.00, description='High performance laptop')
        url = reverse('product-detail', args=[product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Laptop')
