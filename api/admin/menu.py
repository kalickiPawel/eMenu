from django.contrib import admin
from api import models


class MenuAdmin(admin.ModelAdmin):
    model = models.Menu
    list_display = (
        'name',
        'description',
        'created_at',
        'updated_at'
    )


admin.site.register(models.Menu, MenuAdmin)
