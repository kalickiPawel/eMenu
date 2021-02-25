import pytest
from django.contrib.admin.sites import AdminSite
from api import models
from api import admin

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestDishAdmin:
    pytestmark = pytest.mark.django_db

    def test_model_get_name(self):
        site = AdminSite()
        dish_admin = admin.DishAdmin(models.Dish, site)
        assert str(dish_admin) == 'api.DishAdmin', 'Should get the dish admin'
