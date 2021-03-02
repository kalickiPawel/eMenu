from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets, permissions

from api.serializers import MenuSerializer
from api.models import Menu


class MenuViewSet(viewsets.ModelViewSet):
    """
    This ViewSet allow to look at list of Menu cards
    with their dishes.

    For authorized user provides:
    GET, POST, PUT and DELETE actions.
    """
    serializer_class = MenuSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['name', 'created_at', 'updated_at']
    ordering_fields = ['name']
    permission_classes = [permissions.AllowAny, permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAuthenticated]

        return super(self.__class__, self).get_permissions()

    def get_queryset(self):
        queryset = Menu.objects
        query_filter = self.request.query_params.get('ordering', None)

        allow_filters = ['dishes_count']
        allow_filters += [f'-{el}' for el in allow_filters]

        if query_filter in allow_filters:
            if query_filter == r'dishes_count':
                queryset = queryset.annotate(
                    dishes_count=Count('dishes')
                ).order_by(query_filter)

        if self.request.user.is_authenticated:
            return queryset
        else:
            return queryset.annotate(dishes_count=Count('dishes')).filter(dishes_count__gt=0)

    def perform_create(self, serializer):
        serializer.save()
