# from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from api.serializers import MenuSerializer
from api.models import Menu


class MenuViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    The queryset is setup with permission
    """
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'created_at', 'updated_at']

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Menu.objects.all()
        else:
            return Menu.objects.filter(dishes__isnull=False)

    def perform_create(self, serializer):
        serializer.save()

    # return Menu.objects.filter(dishes__isnull=False).annotate(
    #     number_of_dishes=Count('dishes')
    # ).order_by('-number_of_dishes')

    # return Menu.objects.filter(dishes__isnull=False).order_by('name')
