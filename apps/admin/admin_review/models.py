from django.db import models

from apps.reviews.models.review import Review


# Create your models here.
class ReviewProxy(Review):
    def __str__(self):
        return f"{self.author_name}"

    class Meta:
        proxy = True
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
