from django.conf import settings
from django.db import models

class Car(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'машина'
        verbose_name_plural = "машины"


class Moto(models.Model):
    title = models.CharField(max_length=150, verbose_name='название')
    description = models.TextField(verbose_name='описание')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'мотоцикл'
        verbose_name_plural = "мотоциклы"


class Milage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, blank=True, null=True)
    moto = models.ForeignKey(Moto, on_delete=models.CASCADE, blank=True, null=True, related_name='milage')

    year = models.PositiveSmallIntegerField(default=0, verbose_name='год регистрации пробега')
    milage = models.PositiveSmallIntegerField(default=0, verbose_name='пробег')

    def __str__(self):
        return f'{self.car if self.car else self.moto} - {self.milage} ({self.year})'

    class Meta:
        verbose_name = 'пробег'
        verbose_name_plural = 'пробеги'
        ordering = ('year',)