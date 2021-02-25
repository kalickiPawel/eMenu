from api.models import Dish
from rest_framework import serializers


class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = (
            'name',
            'description',
            'created_at',
            'updated_at',
            'price',
            'preparation_time',
            'vegan'
        )
