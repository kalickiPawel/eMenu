from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from api.serializers import DishSerializer
from api.models import Dish


class DishViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions of Dish objects.
    """
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        serializer.save()
