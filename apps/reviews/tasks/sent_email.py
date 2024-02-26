from celery import shared_task


@shared_task
def sent_email(a, b, c):
    print("Письмо отправлено", a, b, c)
