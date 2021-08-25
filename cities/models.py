from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='город')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'город'
        verbose_name_plural = 'города'
        ordering = ('name', )
