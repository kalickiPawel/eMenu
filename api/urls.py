from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import MenuViewSet, DishViewSet

router = DefaultRouter()
router.register(r'cards', MenuViewSet, basename='menu')
router.register(r'dishes', DishViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
