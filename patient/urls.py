from django.urls import path, include
from django.urls import path
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

app_name = 'patient'

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('favicon.ico', RedirectView.as_view(url=staticfiles_storage.url('image/favicon.ico'))),
    
    # Home
    path('', views.home, name='home'),

    # Search
    path('search/', views.search, name='search'),
    path('search/search_results/', views.search_results, name='search_results'),
    
    # Patient Registration
    # path('Patient', Patient, name='Patient'),
    path('patient-registration/', views.patient_registration, name='patient_registration'),
    path('patient/<pk>/', views.patient_detail, name='patient_detail'),
    path('patient-registration/<pk>/', views.patient_update, name='patient_update'),
    path('patient-list/', views.patient_list, name='patient_list'),

    # Treatment
    path('treatment-create/', views.treatment_create, name='treatment_create'),
    path('treatment-list/', views.treatment_list, name='treatment_list'),
    path('treatment-update/<pk>/', views.treatment_update, name='treatment_update'),

    # Disease Information
    path('disease-info-create/', views.disease_info_create, name='disease_info_create'), # <int:patient_id>/
    path('disease-info-list/', views.disease_info_list, name='disease_info_list'),
    path('disease-info-update/<pk>/', views.disease_info_update, name='disease_info_update'),

    # Treatment Prescription
    path('treatment-prescription-create/', views.treatment_prescription_create, name='treatment_prescription_create'),
    path('treatment-prescription/<pk>/', views.treatment_prescription_detail, name='treatment_prescription_detail'),
    path('treatment-prescription-list/', views.treatment_prescription_list, name='treatment_prescription_list'),
    path('treatment-prescription-update/<pk>/', views.treatment_prescription_update, name='treatment_prescription_update'),
    
    # count patient
    path('patient/count_patient', count_patient, name='count_patient'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)