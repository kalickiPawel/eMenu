from django.contrib import admin


from api.models import Dish


class DishAdmin(admin.ModelAdmin):
    model = Dish
    list_display = [
        'name',
        'description',
        'created_at',
        'updated_at',
        'price',
        'preparation_time',
        'vegan',
        'menu_cards'
    ]

    def menu_cards(self, obj):
        return "\n".join([p.name for p in obj.menu.all()])


admin.site.register(Dish, DishAdmin)
