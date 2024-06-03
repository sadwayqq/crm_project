from django.db import models

class Client(models.Model):
    name = models.CharField(max_length=255)
    contact_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField()
    address = models.TextField()

    class Meta:
        app_label = 'clients'  # Явно указываем название приложения

    def __str__(self):
        return self.name
