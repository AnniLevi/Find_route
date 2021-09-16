from django import forms

from cities.models import City
from trains.models import Train


class TrainForm(forms.ModelForm):
    class Meta:
        model = Train
        fields = "__all__"

    name = forms.CharField(
        label='Номер поезда',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите номер поезда'
        })
    )
    travel_time = forms.IntegerField(
        label='Время в пути',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Время в пути"
        })
    )
    from_city = forms.ModelChoiceField(
        label='Откуда',
        queryset=City.objects,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    to_city = forms.ModelChoiceField(
        label='Куда',
        queryset=City.objects,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
