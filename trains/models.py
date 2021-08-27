from django.core.exceptions import ValidationError
from django.db import models

from cities.models import City


class Train(models.Model):
    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ('-name',)

    name = models.CharField(max_length=50, unique=True, verbose_name='Название поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='from_city_set',
        verbose_name='Откуда'
    )
    to_city = models.ForeignKey(
        'cities.City',  # без импорта
        on_delete=models.CASCADE,
        related_name='to_city_set',
        verbose_name='Куда'
    )

    def __str__(self):
        return f'Поезд № {self.name} из города {self.from_city} в город {self.to_city}'

    def clean(self):
        if self.from_city == self.to_city:
            raise ValidationError('Город отправления и город прибытия не должны быть одинаковыми')
        qs = Train.objects.filter(          # Train == self.__class__
            from_city=self.from_city,
            to_city=self.to_city,
            travel_time=self.travel_time
        ).exclude(pk=self.pk)
        if qs.exists():
            raise ValidationError('Такой поезд уже существует')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
