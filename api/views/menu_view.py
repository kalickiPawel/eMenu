from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from rest_framework import viewsets

from api.serializers import MenuSerializer
from api.models import Menu


class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    @method_decorator(login_required)
    def create(self, request, *args, **kwargs):
        return super(MenuViewSet, self).create(request, *args, **kwargs)

    def list(self, request, *args, **kwargs):
        return super(MenuViewSet, self).list(request, *args, **kwargs)
