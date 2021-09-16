from django.db import models
from cities.models import City


class Route(models.Model):
    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ('name',)

    name = models.CharField(max_length=50, unique=True, verbose_name='Название маршрута')
    travel_times = models.PositiveSmallIntegerField(verbose_name='Общее время в пути')
    from_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='route_from_city_set',
        verbose_name='Откуда'
    )
    to_city = models.ForeignKey(
        'cities.City',                          # без импорта
        on_delete=models.CASCADE,
        related_name='route_to_city_set',
        verbose_name='Куда'
    )
    trains = models.ManyToManyField('trains.Train', verbose_name="Поезда")

    def __str__(self):
        return f'Маршрут {self.name} из города {self.from_city} в город {self.to_city}'


