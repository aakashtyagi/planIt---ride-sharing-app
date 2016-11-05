from django.contrib import admin
from models import Trip, Location, ActiveEdu, TripParty, TripCategory, TripPlaces

class TripAdmin(admin.ModelAdmin):
    list_display=['id', 'name']

admin.site.register(Trip, TripAdmin)
admin.site.register(Location)
admin.site.register(ActiveEdu)
admin.site.register(TripParty)
admin.site.register(TripCategory)
admin.site.register(TripPlaces)
