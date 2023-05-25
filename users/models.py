from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    img = models.ImageField(upload_to='profile')

    def __str__(self):
        return f''' Профайл пользователя {self.user.username}'''

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профиль'