from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task
def sent_email(subject, message, recipient):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [recipient],
        fail_silently=False,
    )
