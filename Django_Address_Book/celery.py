'''
from __future__ import absolute_import, unicode_literals
from django.conf import settings
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Django_Address_Book.settings")
app = Celery("Django_Address_Book")
app.config_from_object(settings, namespace="CELERY")
app.autodiscover_tasks()


@app.task(bind=True)
def add(x, y):
    return x + y
'''


import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Address_Book.settings')

app = Celery('Django_Address_Book', backend='redis://redis:6379/0', broker='redis://redis:6379/0')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
