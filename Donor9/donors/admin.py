from django.contrib import admin
from .models import Donor, Location, Donation, SMS, SMSTemplate

class DonorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Donor, DonorAdmin)


class LocationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Location, LocationAdmin)



class DonationAdmin(admin.ModelAdmin):
    pass

admin.site.register(Donation, DonationAdmin)



class SMSAdmin(admin.ModelAdmin):
    pass

admin.site.register(SMS, SMSAdmin)



class SMSTemplateAdmin(admin.ModelAdmin):
    pass

admin.site.register(SMSTemplate, SMSTemplateAdmin)
