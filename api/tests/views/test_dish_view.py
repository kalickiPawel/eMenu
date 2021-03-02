from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from api.views import DishViewSet
from api.models import Menu


class TestDishViewSet(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@test.com', password='top_secret')
        self.menu = Menu.objects.create(name='card1')
        self.valid_data = {
            "name": "Schabowy z ziemniakami",
            "description": "Schabowy wieprzowy z ziemniakami gotowanymi",
            "price": 20.25,
            "preparation_time": 20,
            "vegan": True,
            "menu": [self.menu.id]
        }
        self.invalid_data = {
            "name": "Schabowy z ziemniakami",
            "description": 20.25,
            "price": "Schabowy wieprzowy z ziemniakami gotowanymi",
            "preparation_time": True,
            "vegan": 20,
            "menu": [self.menu.id]
        }

    def test_get_all_dishes_as_anonymous(self):
        request = self.factory.get('dishes')
        request.user = AnonymousUser()

        response = DishViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_all_dishes_as_authenticated(self):
        request = self.factory.get('dishes')
        force_authenticate(request, user=self.user)

        response = DishViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_dish_as_anonymous(self):
        request = self.factory.get('dishes/1')
        request.user = AnonymousUser()

        response = DishViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_one_dish_as_authenticated(self):
        request = self.factory.get('dishes/1')
        force_authenticate(request, user=self.user)

        response = DishViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_dish_as_anonymous_valid(self):
        request = self.factory.post('dishes/', self.valid_data)
        request.user = AnonymousUser()

        response = DishViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_dish_as_authenticated_valid(self):
        request = self.factory.post('dishes/', self.valid_data)
        force_authenticate(request, user=self.user)

        response = DishViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_dish_as_anonymous_invalid(self):
        request = self.factory.post('dishes/', self.invalid_data)
        request.user = AnonymousUser()

        response = DishViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_dish_as_authenticated_invalid(self):
        request = self.factory.post('dishes/', self.invalid_data)
        force_authenticate(request, user=self.user)

        response = DishViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
