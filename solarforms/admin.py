from django.contrib import admin
from .models import SolarDatas

@admin.register(SolarDatas)
class SolarDatasAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'contact_name', 'phone_number', 
                   'preferred_contact_time', 'latest_electric_bill', 'created_at')
    search_fields = ('location_name', 'contact_name', 'phone_number')
    list_filter = ('created_at', 'preferred_contact_time', 'preferred_survey_date')