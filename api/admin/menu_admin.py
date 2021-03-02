from django.contrib import admin

from api.models import Menu


class MenuAdmin(admin.ModelAdmin):
    model = Menu
    list_display = [
        'name',
        'description',
        'created_at',
        'updated_at',
        'dishes_list',
        'dishes_count'
    ]

    def dishes_list(self, obj):
        return "\n".join([p.name for p in obj.dishes.all()])

    def dishes_count(self, obj):
        return obj.dishes.count()


admin.site.register(Menu, MenuAdmin)
