from rest_framework import serializers

from api.models import Menu
from .dish_serializer import DishSerializer


class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = (
            'name',
            'description',
            'created_at',
            'updated_at',
            'dishes',
        )
