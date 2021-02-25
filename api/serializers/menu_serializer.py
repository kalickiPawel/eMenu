from api.models import Menu
from rest_framework import serializers


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = (
            'name',
            'description',
            'created_at',
            'updated_at'
        )
