from django.urls import include, path
from rest_framework import routers
from .views import MenuViewSet, DishViewSet

router = routers.DefaultRouter()
router.register(r'menu', MenuViewSet)
router.register(r'dish', DishViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
