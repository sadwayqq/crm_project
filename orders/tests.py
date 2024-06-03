from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from clients.models import Client
from .models import Order

class OrderTestCase(APITestCase):
    def setUp(self):
        # Создаем клиента для использования в заказах
        self.client_obj = Client.objects.create(name='John Doe', contact_phone='1234567890', email='john@example.com', address='123 Main St')

    def test_create_order(self):
        url = reverse('order-list')
        data = {
            'client': self.client_obj.id,
            'order_date': '2021-01-01',
            'status': 'pending',
            'total': 150.00
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().total, 150.00)

    def test_get_order(self):
        order = Order.objects.create(client=self.client_obj, order_date='2021-01-01', status='pending', total=150.00)
        url = reverse('order-detail', args=[order.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'pending')

    def test_delete_order(self):
        order = Order.objects.create(client=self.client_obj, order_date='2021-01-01', status='pending', total=150.00)
        url = reverse('order-detail', args=[order.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Order.objects.count(), 0)
