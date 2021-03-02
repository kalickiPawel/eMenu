from datetime import datetime
from decimal import Decimal
import random
import string

import pytest
from mixer.backend.django import mixer

from api.models import Menu


@pytest.mark.django_db
class TestDish:
    def test_model(self):
        obj = mixer.blend('api.Dish')
        assert obj.pk == 1, 'Should create a Dish instance'

    def test_model_repr(self):
        obj = mixer.blend('api.Dish', name='dish1')
        assert str(obj) == 'dish1'

    def test_it_has_information_fields(self):
        obj = mixer.blend(
            'api.Dish',
            name='Schabowy z ziemniakami',
            description="Schabowy wieprzowy z ziemniakami gotowanymi",
            price=20.25,
            preparation_time=20,
            vegan=True
        )
        assert isinstance(obj.name, str)
        assert isinstance(obj.description, str)
        assert isinstance(obj.price, Decimal)
        assert isinstance(obj.preparation_time, float)
        assert isinstance(obj.vegan, bool)

        assert obj.name == 'Schabowy z ziemniakami'
        assert obj.description == 'Schabowy wieprzowy z ziemniakami gotowanymi'
        assert obj.price == Decimal(20.25)
        assert obj.preparation_time == 20.0
        assert obj.vegan is True

    def test_it_has_timestamps(self):
        obj = mixer.blend(
            'api.Dish',
            name='Schabowy z ziemniakami',
            description="Schabowy wieprzowy z ziemniakami gotowanymi",
            price=20.25,
            preparation_time=20,
            vegan=True
        )
        assert isinstance(obj.created_at, datetime)
        assert isinstance(obj.updated_at, datetime)

    def test_it_can_be_attached_to_multiple_cards(self):
        obj = mixer.blend(
            'api.Dish',
            name='Schabowy z ziemniakami',
            description="Schabowy wieprzowy z ziemniakami gotowanymi",
            price=20.25,
            preparation_time=20,
            vegan=True
        )
        sample_menu_names = [''.join(random.choice(string.ascii_letters) for _ in range(10)) for _ in range(3)]
        cards = [Menu.objects.create(
            name=sample_menu_names[i]
        ) for i in range(3)]

        for menu in cards:
            menu.dishes.add(obj)

        assert len(cards) == obj.menu.count()
        for menu in cards:
            assert obj in menu.dishes.all()
