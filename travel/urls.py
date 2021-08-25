from django.contrib import admin
from django.urls import path, include
from travel.views import home, about


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cities/', include(('cities.urls', 'cities'))),
    path('about/', about),
    path('', home, name='home'),
]
