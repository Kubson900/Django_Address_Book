from __future__ import absolute_import, unicode_literals
from django.conf import settings
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_Address_Book.settings")
app = Celery("Django_Address_Book")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()

#@app.task(bind=True)
#def add(x, y):
    #return x + y
