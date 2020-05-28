from django.contrib import admin

from .models import Show, Event

# Register your models here.
class ShowAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "year", "eps")

class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "show_id", "episode", "animal", "continent",
                    "location", "time", "description")

admin.site.register(Show, ShowAdmin)
admin.site.register(Event, EventAdmin)