from django.db import models

# Create your models here.
class books(models.Model):
    name = models.CharField(max_length=60)
    title = models.CharField(max_length=50)
    description = models.TextField()
    auther = models.CharField(max_length=50)
    serial_number = models.CharField(max_length=20)
    price = models.IntegerField()

    def __str__(self):
        return self.name