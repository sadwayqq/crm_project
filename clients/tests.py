from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Client

class ClientTestCase(APITestCase):
    def test_create_client(self):
        url = reverse('client-list')
        data = {'name': 'John Doe', 'contact_phone': '1234567890', 'email': 'john@example.com', 'address': '123 Main St'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Client.objects.count(), 1)
        self.assertEqual(Client.objects.get().name, 'John Doe')

    def test_get_client(self):
        client = Client.objects.create(name='John Doe', contact_phone='1234567890', email='john@example.com', address='123 Main St')
        url = reverse('client-detail', args=[client.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'john@example.com')

    def test_delete_client(self):
        client = Client.objects.create(name='John Doe', contact_phone='1234567890', email='john@example.com', address='123 Main St')
        url = reverse('client-detail', args=[client.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Client.objects.count(), 0)
