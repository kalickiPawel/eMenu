from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'created_at', 'updated_at')

    def __str__(self):
        return self.name
