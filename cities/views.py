from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from cities.models import City
from cities.forms import HtmlForm, CityForm

__all__ = (
    'home',
    'CityDetailView',

)


def home(request, pk=None):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
    # if pk:
        # city = City.objects.filter(pk=pk).first()
        # city = get_object_or_404(City, pk=pk)
        # context = {'object': city}
        # return render(request, 'cities/detail.html', context)
    form = CityForm()
    qs = City.objects.all()
    context = {'objects_list': qs, 'form': form}
    return render(request, 'cities/home.html', context)


class CityDetailView(DetailView):
    queryset = City.objects
    template_name = 'cities/detail.html'
