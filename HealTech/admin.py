from django.contrib import admin

from .models import Appointment, Drug, SuggestionsForAppointment


# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['for_doctor', 'from_patient', 'date', 'time', 'posted_at']
    # filter_horizontal = ['illness', 'suggested_drugs']


class DrugAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    filter_horizontal = ['for_illness']


class SuggestionsForAppointmentAdmin(admin.ModelAdmin):
    list_display = ['suggestion_for', 'date']
    filter_horizontal = ['illness', 'drugs']


admin.site.register(SuggestionsForAppointment, SuggestionsForAppointmentAdmin)
admin.site.register(Appointment, AppointmentAdmin)
admin.site.register(Drug, DrugAdmin)
