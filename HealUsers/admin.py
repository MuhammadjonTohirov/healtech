from django.contrib import admin

from .models import Doctor, Patient, JobType, TypeOfIllness, CategoryOfDocs


# Register your models here.

class JobTypeAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class DoctorAdmin(admin.ModelAdmin):
    list_display = ['user', 'description', 'works_from', 'works_to']
    filter_horizontal = ['pos']


class PatientAdmin(admin.ModelAdmin):
    list_display = ['user', 'birth_date', 'image', 'registered', 'updated']
    search_fields = ['user']
    # filter_horizontal = ['illness']


class TypeOfIllnessAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class CategoryOfDocsAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


admin.site.register(CategoryOfDocs, CategoryOfDocsAdmin)
admin.site.register(TypeOfIllness, TypeOfIllnessAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(JobType, JobTypeAdmin)
