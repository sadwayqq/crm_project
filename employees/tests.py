from django.test import TestCase

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Employee

class EmployeeTestCase(APITestCase):
    def test_create_employee(self):
        url = reverse('employee-list')
        data = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'position': 'Manager',
            'hire_date': '2020-02-20'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 1)
        self.assertEqual(Employee.objects.get().first_name, 'Jane')

    def test_get_employee(self):
        employee = Employee.objects.create(first_name='Jane', last_name='Doe', position='Manager', hire_date='2020-02-20')
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['last_name'], 'Doe')

    def test_delete_employee(self):
        employee = Employee.objects.create(first_name='Jane', last_name='Doe', position='Manager', hire_date='2020-02-20')
        url = reverse('employee-detail', args=[employee.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Employee.objects.count(), 0)
