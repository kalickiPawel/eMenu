import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser
from api.views import DishViewSet

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestDishViewSet:
    pytestmark = pytest.mark.django_db

    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = DishViewSet.as_view({'get': 'list'})(req)
        assert resp.status_code == 200, 'Should be callable by anyone'

    def test_authenticated_user(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = DishViewSet.as_view({'get': 'create'})(req)
        assert 'login' in resp.url, 'Should be callable by authenticated user'
