import pytest
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser

from api.views import MenuViewSet

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestMenuViewSet:
    pytestmark = pytest.mark.django_db

    def test_anonymous(self):
        req = RequestFactory().get('/')
        resp = MenuViewSet.as_view({'get': 'list'})(req)
        assert resp.status_code == 200, 'Should be callable by anyone'

    def test_authenticated_user(self):
        req = RequestFactory().get('/')
        req.user = AnonymousUser()
        resp = MenuViewSet.as_view({'get': 'create'})(req)
        assert 'login' in resp.url, 'Should be callable by authenticated user'
