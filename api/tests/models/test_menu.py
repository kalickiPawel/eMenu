from datetime import datetime
import random
import string

import pytest
from mixer.backend.django import mixer

from api.models import Dish


@pytest.mark.django_db
class TestMenu:
    def test_model(self):
        obj = mixer.blend('api.Menu')
        assert obj.pk == 1, 'Should create a Menu instance'

    def test_it_has_information_fields(self):
        obj = mixer.blend(
            'api.Menu',
            name='Karta jesienna',
            description="Sezonowa karta dań przygotowana specjalna na ten rok",
        )
        assert isinstance(obj.name, str)
        assert isinstance(obj.description, str)
        assert obj.name == 'Karta jesienna'
        assert obj.description == "Sezonowa karta dań przygotowana specjalna na ten rok"

    def test_it_has_timestamps(self):
        obj = mixer.blend(
            'api.Menu',
            name='Karta jesienna',
            description="Sezonowa karta dań przygotowana specjalna na ten rok",
        )
        assert isinstance(obj.created_at, datetime)
        assert isinstance(obj.updated_at, datetime)

    def test_it_can_be_attached_to_multiple_cards(self):
        obj = mixer.blend(
            'api.Menu',
            name='Karta jesienna',
            description="Sezonowa karta dań przygotowana specjalna na ten rok",
        )
        sample_dish_names = [''.join(random.choice(string.ascii_letters) for _ in range(10)) for _ in range(3)]
        dishes = [Dish.objects.create(
            name=sample_dish_names[i],
            price=20.00,
            preparation_time=20
        ) for i in range(3)]

        for dish in dishes:
            dish.menu.add(obj)

        assert len(dishes) == obj.dishes.count()
        for dish in dishes:
            assert obj in dish.menu.all()
