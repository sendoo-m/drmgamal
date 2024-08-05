from django import forms
from dataclasses import fields
from datetime import date
from django import forms
from .models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget # to Import edit text box and tool
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name', 'age', 'occupation', 'file_number', 'mobile_number', 'birthdate', 'gender')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Patient Information',
                'name',
                'age',
                'occupation',
                'gender',
                'mobile_number'
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )

class TreatmentForm(forms.ModelForm):
    class Meta:
        model = Treatment
        fields = ('treatment', 'description', 'company', 'dosage')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Treatment Information',
                'treatment',
                'description',
                'company',
                'dosage'
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )

class treatmentsearchForm(forms.Form):
    search_query = forms.CharField(
        label='Search', 
        required=False, 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by treatment, company',
            'class': 'form-control',
        })
    )
    company = forms.ModelChoiceField(
        queryset=Treatment.objects.all(), 
        label='Company', 
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

class patientsearchForm(forms.Form):
    search_query = forms.CharField(
        label='Search', 
        required=False, 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by Name, Mobile Number',
            'class': 'form-control',
        })
    )
    mobile_number = forms.ModelChoiceField(
        queryset=Patient.objects.all(), 
        label='mobile number', 
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

class disease_infoearchForm(forms.Form):
    search_query = forms.CharField(
        label='Search', 
        required=False, 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by Name, Mobile Number',
            'class': 'form-control',
        })
    )
    mobile_number = forms.ModelChoiceField(
        queryset=Patient.objects.all(), 
        label='mobile number', 
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

class treatmentprescriptionsearchForm(forms.Form):
    search_query = forms.CharField(
        label='Search', 
        required=False, 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Search by Name, Company',
            'class': 'form-control',
        })
    )
    mobile_number = forms.ModelChoiceField(
        queryset=Patient.objects.all(), 
        label='company', 
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control',
        })
    )

class DiseaseInfoForm(forms.ModelForm):
    class Meta:
        model = DiseaseInfo
        fields = ('patient', 'medical_history', 'complaint', 'diagnosis', 'temp', 'weight', 'doctor_notes', 'treatments1', 'treatments2', 'treatments3', 'treatments4', 'treatments5', 'treatments6', 'treatments7')
        widgets = {
            'medical_history': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}),
            'complaint': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}),
            'diagnosis': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}),
            'doctor_notes': SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Disease Information',
                'patient',
                'medical_history',
                'complaint',
                'diagnosis',
                'temp',
                'weight',
                'doctor_notes',
                'treatments1',
                'treatments2',
                'treatments3',
                'treatments4',
                'treatments5',
                'treatments6',
                'treatments7',
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )

class TreatmentPrescriptionForm(forms.ModelForm):
    class Meta:
        model = TreatmentPrescription
        fields = ('patient', 'treatments1', 'treatments2', 'treatments3', 'treatments4', 'treatments5', 'treatments6', 'treatments7', 'dosage_and_times', 'doctor_recommendations', 'next_consultation_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Treatment Prescription',
                'patient',
                'treatments1',
                'treatments2',
                'treatments3',
                'treatments4',
                'treatments5',
                'treatments6',
                'treatments7',
                'dosage_and_times',
                'doctor_recommendations',
                'next_consultation_date'
            ),
            ButtonHolder(
                Submit('submit', 'Submit')
            )
        )