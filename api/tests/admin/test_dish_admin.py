import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer

from api import models
from api import admin

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestDishAdmin:
    pytestmark = pytest.mark.django_db

    def test_model_get_name(self):
        site = AdminSite()
        dish_admin = admin.DishAdmin(models.Menu, site)
        assert str(dish_admin) == 'api.DishAdmin', 'Should get the menu admin'

    def test_model_get_all_menu_cards_string(self):
        site = AdminSite()
        dish_admin = admin.DishAdmin(models.Dish, site)
        obj = mixer.blend(
            'api.Dish',
            name='Schabowy z ziemniakami',
            description="Schabowy wieprzowy z ziemniakami gotowanymi",
            price=20.25,
            preparation_time=20,
            vegan=True
        )
        assert dish_admin.lookup_allowed('menu_cards', dish_admin.menu_cards(obj))
