from django.contrib import admin
from trains.models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    class Meta:
        model = Train

    list_display = ('name', 'from_city', 'to_city', 'travel_time')
    list_editable = ('travel_time',)
    list_display_links = ('name',)

# admin.site.register(Train)
