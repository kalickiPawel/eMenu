from __future__ import absolute_import, unicode_literals

import datetime

from celery import shared_task

NUM_DAYS = 1

# from django.core.mail import send_mail
# from django.contrib.auth.models import User
# from django.db.models import Count
#
# from api.models import Dish, Menu


@shared_task
def send_email_task():
    # dishes_created = get_dishes(get_creation(Dish))
    # dishes_updated = get_dishes(get_updation(Dish))
    #
    # cards_created = get_cards(get_creation(Menu))
    # cards_updated = get_cards(get_updation(Menu))
    #
    # message = ""
    # message += f"Dzień: {datetime.datetime.today().strftime('%d %B %Y')}"
    # message += "\n---"
    # message += "\n---"
    # message += "\nStworzone poprzedniego dnia:\n"
    # message += "Dania: \n"
    #
    # for row in zip(*([key] + value for key, value in sorted(dishes_created.items()))):
    #     message += ' '.join(["{:>15}".format(el) for el in row])
    #     message += '\n'
    #
    # message += "\n---\n"
    # message += "Karty menu: \n"
    #
    # for row in zip(*([key] + value for key, value in sorted(cards_created.items()))):
    #     message += ' '.join(["{:>15}".format(el) for el in row])
    #     message += '\n'
    #
    # message += "\n---"
    # message += "\n---"
    #
    # message += "\nZaktualizowane poprzedniego dnia:\n"
    # message += "Dania: \n"
    #
    # for row in zip(*([key] + value for key, value in sorted(dishes_updated.items()))):
    #     message += ' '.join(["{:>15}".format(el) for el in row])
    #     message += '\n'
    #
    # message += "\n---\n"
    # message += "Karty menu: \n"
    #
    # for row in zip(*([key] + value for key, value in sorted(cards_updated.items()))):
    #     message += ' '.join(["{:>15}".format(el) for el in row])
    #     message += '\n'
    #
    # send_mail(
    #     "eMenu newsletter! Today's update",
    #     message,
    #     'support@eMenu.com',
    #     recipient_list=[user.email for user in User.objects.all()]
    # )
    return None


# def get_dishes(data):
#     dish_fields = ['name', 'description', 'price', 'preparation_time', 'vegan']
#     dishes = dict.fromkeys(dish_fields)
#     for dish in dishes:
#         dishes[dish] = [x.get(dish) for x in data]
#     return dishes
#
#
# def get_cards(data):
#     menu_fields = ['name', 'description']
#     cards = dict.fromkeys(menu_fields)
#     for card in cards:
#         cards[card] = [x.get(card) for x in data]
#     return cards


# def get_creation(model):
#     creation = model.objects.filter(
#         created_at__lte=datetime.datetime.today(),
#         created_at__gt=datetime.datetime.today() - datetime.timedelta(days=NUM_DAYS)
#     ).values().annotate(count=Count('id'))
#     return creation
#
#
# def get_updation(model):
#     updation = model.objects.filter(
#         updated_at__lte=datetime.datetime.today(),
#         updated_at__gt=datetime.datetime.today() - datetime.timedelta(days=NUM_DAYS)
#     ).values().annotate(count=Count('id'))
#     return updation
