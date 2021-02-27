from django.db import models
from api.models import Menu


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    preparation_time = models.FloatField()
    vegan = models.BooleanField()

    menu = models.ForeignKey(Menu, related_name='dishes', on_delete=models.CASCADE)

    class Meta:
        ordering = ('name', 'created_at', 'updated_at')

    def __str__(self):
        return self.name
