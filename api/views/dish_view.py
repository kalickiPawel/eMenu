from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets

from api.serializers import DishSerializer
from api.models import Dish


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

    @method_decorator(login_required)
    def create(self, request, *args, **kwargs):
        return super(DishViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(DishViewSet, self).list(request, *args, **kwargs)
