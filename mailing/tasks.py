from celery import shared_task
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@shared_task
def send_email(dict_user):
    template = render_to_string('mailing/email_template.html', {'username': dict_user['username']})

    email = EmailMessage(
        'Thank You for creating account!',
        template,
        settings.EMAIL_HOST_USER,
        [dict_user['email']],
    )
    email.fail_silently = False
    email.send()
