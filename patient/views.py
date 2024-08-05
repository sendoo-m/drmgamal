from django.shortcuts import render, get_object_or_404, redirect
from patient.models import *
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.db.models.query_utils import Q
from django.core.paginator import Paginator
from django.contrib.auth import views as auth_views

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

# Create your views here.

# ---------------------------------
# Add Patient to DB From HTML File and this file come from forms
# ---------------------------------

def edit_patient(request, id): #def edit_patient in urls
    edit = get_object_or_404(Add_patient, idnational=id)
    if request.method == 'POST': #POST in form edit_patient in edit_patient html
        formtohtml = Update_PatientForm(request.POST, instance=edit) # edit_patient come from forms.py
        if formtohtml.is_valid():
            formtohtml.save() # to save data in forms
            messages.success(request, 'Update Patient Successful.')
            
    else:
        formtohtml= Update_PatientForm(instance=edit)
    return render(request,'patient/edit.html',{'updatehtml':formtohtml}) # edit_patient From forms.py 
# ---------------------------------
#  END Add Patient to DB Code
# ---------------------------------

# ------------------
#  Count Patients
# ------------------

def count_patient(request):
    patient_count   = Add_patient.objects.all() # to get all object from db
    patient_counts  = patient_count.count() # to count All objects in db
    query           = Add_patient.objects.filter().order_by('date') # to views by orders date
    context = {
        'patient_counts': patient_counts, # patient_counts to use in HTML files query my varibal in above 
        'query' : query,
    }
    return render(request,'patient/count_patient.html', context)
# ------------------
#  End Count Patients
# ------------------

@never_cache
@login_required
def home(request):
    return render(request, 'patient/home.html')


# Patient Registration Views
@never_cache
@login_required
def patient_registration(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient registered successfully!')
            return redirect('patient:patient_list')
    else:
        form = PatientForm()
    return render(request, 'patient/patient_registration.html', {'form': form})

@never_cache
@login_required
def patient_detail(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    return render(request, 'patient/patient_detail.html', {'patient': patient})

def patient_update(request, pk):
    patient = Patient.objects.get(pk=pk)
    if request.method == 'POST':
        form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Patient updated successfully!')
            return redirect('patient:patient_list')
    else:
        form = PatientForm(instance=patient)
    return render(request, 'patient/patient_update.html', {'form': form})

@never_cache
@login_required
def patient_list(request):
    # Retrieve all Patients
    patients = Patient.objects.all()

    # Create an instance of the search form
    search_form = patientsearchForm(request.GET)

    # Apply search filter if provided
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        mobile_number = search_form.cleaned_data.get('mobile_number')
        name = search_form.cleaned_data.get('name')
        
        if search_query:
            patients = patients.filter(
                Q(name__iexact=search_query) | Q(mobile_number__iexact=search_query)
            )
        
    # Paginate the Patient list
    paginator = Paginator(patients, 10)  # Show 10 patients per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        
        'patients': patients,
        'page_obj': page_obj,
        'search_form': search_form,
    }
    return render(request, 'patient/patient_list.html', context)

# Treatment Views
@never_cache
@login_required
def treatment_create(request):
    if request.method == 'POST':
        form = TreatmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Treatment created successfully!')
            return redirect('patient:treatment_list')
    else:
        form = TreatmentForm()
    return render(request, 'patient/treatment_create.html', {'form': form})

@never_cache
@login_required
def treatment_list(request):
    # Retrieve all treatments
    treatments = Treatment.objects.all()

    # Create an instance of the search form
    search_form = treatmentsearchForm(request.GET)

    # Apply search filter if provided
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        treatment = search_form.cleaned_data.get('treatment')
        company = search_form.cleaned_data.get('company')
        
        if search_query:
            treatments = treatments.filter(
                Q(treatment__iexact=search_query) | Q(company__iexact=search_query)
            )
        
    # Paginate the treatment list
    paginator = Paginator(treatments, 10)  # Show 10 treatments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        
        'treatments': treatments,
        'page_obj': page_obj,
        'search_form': search_form,
    }
    return render(request, 'patient/treatment_list.html', context)

@never_cache
@login_required
def treatment_update(request, pk):
    treatment = Treatment.objects.get(pk=pk)
    if request.method == 'POST':
        form = TreatmentForm(request.POST, instance=treatment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Treatment updated successfully!')
            return redirect('patient:treatment_list')
    else:
        form = TreatmentForm(instance=treatment)
    return render(request, 'patient/treatment_update.html', {'form': form})

# def disease_info_create(request): # , patient_id
#     patient = get_object_or_404(Patient) # , pk=patient_id
#     if request.method == 'POST':
#         form = DiseaseInfoForm(request.POST)
#         if form.is_valid():
#             disease_info = form.save(commit=False)
#             disease_info.patient = patient
#             disease_info.save()
#             messages.success(request, 'Disease information created successfully!')
#             return redirect('disease_info_list')  # , patient_id=patient.id
#     else:
#         form = DiseaseInfoForm()
#     return render(request, 'patient/disease_info_create.html', {'form': form, 'patient': patient})

@never_cache
@login_required
def disease_info_create(request):
    if request.method == 'POST':
        form = DiseaseInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Disease info created successfully!')
            return redirect('patient:disease_info_list')
    else:
        form = DiseaseInfoForm()
    return render(request, 'patient/disease_info_create.html', {'form': form})

# @never_cache
# @login_required
# def disease_info_list(request):
#     disease_info = DiseaseInfo.objects.all()
#     return render(request, 'patient/disease_info_list.html', {'disease_info': disease_info})
@never_cache
@login_required
def disease_info_list(request):
    # Retrieve all treatments
    disease_info = DiseaseInfo.objects.all()

    # Create an instance of the search form
    search_form = disease_infoearchForm(request.GET)

    # Apply search filter if provided
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        # diseaseInfo = search_form.cleaned_data.get('diseaseInfo')
        patient = search_form.cleaned_data.get('patient')
        
        if search_query:
            diseaseInfos = disease_info.filter(
                Q(treatment__iexact=search_query) | Q(company__iexact=search_query)
            )
        
    # Paginate the treatment list
    paginator = Paginator(disease_info, 10)  # Show 10 DiseaseInfo per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        
        'disease_info': disease_info,
        'page_obj': page_obj,
        'search_form': search_form,
    }
    return render(request, 'patient/disease_info_list.html', context)

@never_cache
@login_required
def disease_info_update(request, pk):
    disease_info = DiseaseInfo.objects.get(pk=pk)
    if request.method == 'POST':
        form = DiseaseInfoForm(request.POST, instance=disease_info)
        if form.is_valid():
            form.save()
            messages.success(request, 'Disease information updated successfully!')
            return redirect('patient:patient_list')
    else:
        form = DiseaseInfoForm(instance=disease_info)
    return render(request, 'patient/disease_info_update.html', {'form': form})

# Treatment Prescription Views
@never_cache
@login_required
def treatment_prescription_create(request):
    if request.method == 'POST':
        form = TreatmentPrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Treatment prescription created successfully!')
            return redirect('patient:treatment_prescription_list')
    else:
        form = TreatmentPrescriptionForm()
    return render(request, 'patient/treatment_prescription_create.html', {'form': form})

@never_cache
@login_required
def treatment_prescription_detail(request, pk):
    treatment_prescription_detail = get_object_or_404(TreatmentPrescription, pk=pk)
    return render(request, 'patient/treatment_prescription_detail.html', {'treatment_prescription_detail': treatment_prescription_detail})

# @never_cache
# @login_required
# def treatment_prescription_list(request):
#     treatments = TreatmentPrescription.objects.all()       
#     paginator = Paginator(treatments, 10)  # Show 10 treatments per page
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'treatments': treatments,
#         'page_obj': page_obj,
#     }
#     return render(request, 'patient/treatment_prescription_list.html', context)

@never_cache
@login_required
def treatment_prescription_list(request):
    # Retrieve all treatments
    treatments = TreatmentPrescription.objects.all()

    # Create an instance of the search form
    search_form = treatmentprescriptionsearchForm(request.GET)

    # Apply search filter if provided
    if search_form.is_valid():
        search_query = search_form.cleaned_data.get('search_query')
        treatment = search_form.cleaned_data.get('treatment')
        company = search_form.cleaned_data.get('company')
        
        if search_query:
            treatments = treatments.filter(
                Q(treatment__iexact=search_query) | Q(company__iexact=search_query)
            )
        
    # Paginate the treatment list
    paginator = Paginator(treatments, 10)  # Show 10 treatments per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        
        'treatments': treatments,
        'page_obj': page_obj,
        'search_form': search_form,
    }
    return render(request, 'patient/treatment_prescription_list.html', context)




@never_cache
@login_required
def treatment_prescription_update(request, pk):
    treatment_prescription = TreatmentPrescription.objects.get(pk=pk)
    if request.method == 'POST':
        form = TreatmentPrescriptionForm(request.POST, instance=treatment_prescription)
        if form.is_valid():
            form.save()
            messages.success(request, 'Treatment prescription updated successfully!')
            return redirect('patient:treatment_prescription_list')
    else:
        form = TreatmentPrescriptionForm(instance=treatment_prescription)
    return render(request, 'patient/treatment_prescription_update.html', {'form': form})


@never_cache
@login_required
def search(request):
    query = request.GET.get('q')
    if query:
        patients = Patient.objects.filter(name__icontains=query) | Patient.objects.filter(mobile_number__icontains=query)
    else:
        patients = Patient.objects.none()  # return an empty queryset
    return render(request, 'patient/search.html', {'patients': patients})

@never_cache
@login_required
def search_results(request):
   
    queryfromhtml=request.GET['q'] # queryfromhtml to def request q and q come from html search field
    if queryfromhtml:

        multple_q = Q(Q(name__iexact=queryfromhtml) | Q(mobile_number__iexact=queryfromhtml)) # def multple_q and Q to allow search 2 fields
        query = Patient.objects.filter(multple_q) # to do my search multple
        context={
            'patients':query # regdr to use in HTML files query my varibal in above 
        }
    else:
        context={}
    return render(request, 'patient/search_results.html', context)

