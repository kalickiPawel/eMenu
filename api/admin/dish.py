from django.contrib import admin
from api import models


class DishAdmin(admin.ModelAdmin):
    model = models.Dish
    list_display = (
        'name',
        'description',
        'created_at',
        'updated_at',
        'price',
        'preparation_time',
        'vegan',
        'menu'
    )


admin.site.register(models.Dish, DishAdmin)
