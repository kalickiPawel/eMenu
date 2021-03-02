import pytest
from django.contrib.admin.sites import AdminSite
from mixer.backend.django import mixer

from api import models
from api import admin

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestMenuAdmin:
    pytestmark = pytest.mark.django_db

    def test_model_get_name(self):
        site = AdminSite()
        menu_admin = admin.MenuAdmin(models.Menu, site)
        assert str(menu_admin) == 'api.MenuAdmin', 'Should get the menu admin'

    def test_model_get_all_dishes_string(self):
        site = AdminSite()
        menu_admin = admin.MenuAdmin(models.Menu, site)
        obj = mixer.blend(
            'api.Menu',
            name='Karta jesienna',
            description="Sezonowa karta dań przygotowana specjalna na ten rok",
        )
        assert menu_admin.lookup_allowed('dishes_list', menu_admin.dishes_list(obj))

    def test_model_get_dishes_count(self):
        site = AdminSite()
        menu_admin = admin.MenuAdmin(models.Menu, site)
        obj = mixer.blend(
            'api.Menu',
            name='Karta jesienna',
            description="Sezonowa karta dań przygotowana specjalna na ten rok",
        )
        assert menu_admin.lookup_allowed('dishes_count', menu_admin.dishes_count(obj))
