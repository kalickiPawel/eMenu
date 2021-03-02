from django.contrib.auth.models import User, AnonymousUser
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate

from api.views import MenuViewSet
from api.models import Dish


class TestMenuViewSet(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(username='jacob', email='jacob@test.com', password='top_secret')
        self.dish = Dish.objects.create(
            name="Schabowy z ziemniakami",
            description="Schabowy wieprzowy z ziemniakami gotowanymi",
            price=20.25,
            preparation_time=20,
            vegan=True
        )
        self.valid_data = {
            "name": "Karta sezonowa",
            "description": "To jest jesienna karta"
        }
        self.invalid_data = {
            "name": 20.20,
            "description": True
        }

    def test_get_all_menu_cards_as_anonymous(self):
        request = self.factory.get('api/cards')
        request.user = AnonymousUser()

        response = MenuViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_menu_cards_as_authenticated(self):
        request = self.factory.get('cards')
        force_authenticate(request, user=self.user)

        response = MenuViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_menu_card_as_anonymous(self):
        request = self.factory.get('cards/1')
        request.user = AnonymousUser()

        response = MenuViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_one_menu_card_as_authenticated(self):
        request = self.factory.get('dishes/1')
        force_authenticate(request, user=self.user)

        response = MenuViewSet.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_menu_card_as_anonymous_valid(self):
        request = self.factory.post('dishes/', self.valid_data)
        request.user = AnonymousUser()

        response = MenuViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_menu_card_as_authenticated_valid(self):
        request = self.factory.post('cards/', self.valid_data)
        force_authenticate(request, user=self.user)

        response = MenuViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_menu_card_as_anonymous_invalid(self):
        request = self.factory.post('cards/', self.invalid_data)
        request.user = AnonymousUser()

        response = MenuViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_menu_card_as_authenticated_invalid(self):
        request = self.factory.post('cards/', self.invalid_data)
        force_authenticate(request, user=self.user)

        response = MenuViewSet.as_view({'post': 'create'})(request)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
