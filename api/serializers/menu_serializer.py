from rest_framework import serializers

from api.models import Menu
from .dish_serializer import DishSerializer


class MenuSerializer(serializers.ModelSerializer):
    dishes = DishSerializer(many=True, read_only=True)
    dishes_count = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = (
            'name',
            'description',
            'created_at',
            'updated_at',
            'dishes_count',
            'dishes',
        )

    def get_dishes_count(self, obj):
        return obj.dishes.count()
