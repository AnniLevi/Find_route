from django import forms
from cities.models import City
from routes.models import Route
from trains.models import Train


class RouteForm(forms.Form):
    from_city = forms.ModelChoiceField(
        label='Откуда',
        queryset=City.objects,
        widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'})
    )
    to_city = forms.ModelChoiceField(
        label='Куда',
        queryset=City.objects,
        widget=forms.Select(attrs={'class': 'form-control js-example-basic-single'})
    )
    cities = forms.ModelMultipleChoiceField(
        label='Через города',
        queryset=City.objects,
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control js-example-basic-multiple'})
    )
    travelling_time = forms.IntegerField(
        label='Время в пути',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': "Время в пути"
        })
    )


class RouteModelForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = '__all__'

    name = forms.CharField(
        label='Название маршрута',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите навание маршрута'
        })
    )
    from_city = forms.ModelChoiceField(
        queryset=City.objects,
        widget=forms.HiddenInput()
    )
    to_city = forms.ModelChoiceField(
        queryset=City.objects,
        widget=forms.HiddenInput()
    )
    trains = forms.ModelMultipleChoiceField(
        queryset=Train.objects,
        required=False,
        widget=forms.SelectMultiple(attrs={'class': 'form-control d-none'})
    )
    travel_times = forms.IntegerField(
        widget=forms.HiddenInput()
    )
