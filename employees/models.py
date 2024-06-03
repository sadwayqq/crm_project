from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()

    class Meta:
        app_label = 'employees'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
