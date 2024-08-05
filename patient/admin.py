from django.contrib import admin
from django.utils.html import mark_safe
from django_summernote.admin import SummernoteModelAdmin    # to import edit text box and tool
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export.fields import Field
from .models import *


class PatientAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('name', 'age', 'file_number', 'mobile_number')
    search_fields = ('name', 'file_number')
    list_filter = ['file_number']
    # summernote_fields = ['diagnosis','treatment','note','wt'] # to edit text box and tool

class TreatmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('treatment', 'description', 'company', 'dosage')
    search_fields = ('treatment',)

class DiseaseInfoAdmin(SummernoteModelAdmin):
    list_display = ('patient', 'medical_history', 'complaint', 'diagnosis', 'temp', 'weight', 'doctor_notes')
    search_fields = ('patient__name',)
    summernote_fields = ('medical_history', 'complaint', 'diagnosis', 'doctor_notes')

class TreatmentPrescriptionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'dosage_and_times', 'doctor_recommendations', 'next_consultation_date')
    search_fields = ('patient__name',)

admin.site.register(Patient, PatientAdmin)
admin.site.register(Treatment, TreatmentAdmin)
admin.site.register(DiseaseInfo, DiseaseInfoAdmin)
admin.site.register(TreatmentPrescription, TreatmentPrescriptionAdmin)