import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestMenu:
    pytestmark = pytest.mark.django_db

    def test_model(self):
        obj = mixer.blend('api.Menu')
        assert obj.pk == 1, 'Should create a Menu instance'

    def test_model_name(self):
        obj = mixer.blend('api.Menu', name='Sezonowa karta dań')
        assert str(obj) == 'Sezonowa karta dań', 'Should represent the menu card by its name'
