from django.contrib import admin
from .models import Donor, Location

class DonorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Donor, DonorAdmin)


class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)
