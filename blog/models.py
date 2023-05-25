from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class News(models.Model):
    'Модель Статьи'
    title = models.CharField(max_length=128, verbose_name='Название статьи')
    text = models.TextField(blank=True, verbose_name='Описание')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата публикации')
    author = models.ForeignKey(User, verbose_name='Имя автора', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title
