import pytest
from mixer.backend.django import mixer

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestDish:
    pytestmark = pytest.mark.django_db

    def test_model(self):
        obj = mixer.blend('api.Dish')
        assert obj.pk == 1, 'Should create a Dish instance'

    def test_model_name(self):
        obj = mixer.blend('api.Dish', name='Schabowy z ziemniakami')
        assert str(obj) == 'Schabowy z ziemniakami', 'Should represent the dish by its name'
