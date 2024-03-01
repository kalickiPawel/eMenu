from __future__ import absolute_import, unicode_literals

import os

from celery import Celery
from celery.schedules import crontab

from api.tasks import send_email_task

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "eMenu.settings")

app = Celery("eMenu")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.conf.update(
    enable_utc=True,
    timezone='Europe/Warsaw',
)


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Executes everyday morning at 10:00 a.m.
    sender.add_periodic_task(
        crontab(hour=10, minute=00, day_of_week=','.join(str(i) for i in range(7))),
        send_email_task(),
    )


app.autodiscover_tasks()
