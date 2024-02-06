from django.db import models

from apps.blog.models.posts import Post


# Create your models here.
class PostProxy(Post):
    def __str__(self):
        return self.name

    class Meta:
        proxy = True
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
