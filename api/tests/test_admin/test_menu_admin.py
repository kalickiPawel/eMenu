import pytest
from django.contrib.admin.sites import AdminSite
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
