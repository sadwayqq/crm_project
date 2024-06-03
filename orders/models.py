from django.db import models
from clients.models import Client  # Импорт модели клиента, если связь существует

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_date = models.DateField()
    status = models.CharField(max_length=100)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'orders'

    def __str__(self):
        return f"Order {self.id} - {self.status}"
