from django.contrib import admin
from api import models


class MenuAdmin(admin.ModelAdmin):
    model = models.Menu
    list_display = (
        'name',
        'description',
        'created_at',
        'updated_at',
        'dishes_count'
    )

    def dishes_count(self, obj):
        return obj.dishes.count()


admin.site.register(models.Menu, MenuAdmin)
