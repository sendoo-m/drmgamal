from django.db import models
from unicodedata import name


# Create your models here.

# old data system 

GENDER = (
    ('Male', 'Male'),
    ('Female','Female')
)

class Patient(models.Model):
    file_number     = models.IntegerField(verbose_name='File Number', auto_created = True, serialize = True)
    name            = models.CharField(max_length=250, verbose_name='Name', null=False, blank=True)
    occupation      = models.CharField(max_length=250, verbose_name='Occupation', null=False, blank=True)
    age             = models.IntegerField()
    birthdate       = models.DateField(verbose_name='Birth Date', null=False, blank=True)
    gender          = models.CharField(max_length=10, choices=(GENDER), default=('Male'),null=False, blank=True)
    mobile_number   = models.CharField(max_length=20, verbose_name='Phone Number',null=False, blank=True, unique=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "registration"
        verbose_name_plural = "registrations"

class Treatment(models.Model):
    treatment = models.CharField(max_length=250, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    company = models.CharField(max_length=250, null=True, blank=True)
    dosage = models.CharField(max_length=250, null=True, blank=True)

    def __str__(self):
        return self.treatment

class DiseaseInfo(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    today_date = models.DateField(auto_now_add=True, verbose_name='Today Date')
    medical_history = models.TextField(null=True, blank=True)
    complaint = models.TextField(null=True, blank=True)
    diagnosis = models.TextField(null=True, blank=True)
    temp = models.CharField(max_length=250, null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    doctor_notes = models.TextField(null=True, blank=True)
    treatments1 = models.ForeignKey(Treatment, related_name='Treatments_Needs' , null=True, blank=True, on_delete=models.CASCADE)
    treatments2 = models.ForeignKey(Treatment, related_name='Treatments_Needs2', null=True, blank=True, on_delete=models.CASCADE)
    treatments3 = models.ForeignKey(Treatment, related_name='Treatments_Needs3', null=True, blank=True, on_delete=models.CASCADE)
    treatments4 = models.ForeignKey(Treatment, related_name='Treatments_Needs4', null=True, blank=True, on_delete=models.CASCADE)
    treatments5 = models.ForeignKey(Treatment, related_name='Treatments_Needs5', null=True, blank=True, on_delete=models.CASCADE)
    treatments6 = models.ForeignKey(Treatment, related_name='Treatments_Needs6', null=True, blank=True, on_delete=models.CASCADE)
    treatments7 = models.ForeignKey(Treatment, related_name='Treatments_Needs7', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.patient.name

class TreatmentPrescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    treatments1 = models.ForeignKey(Treatment, related_name='treatment_prescriptions', null=True, blank=True, on_delete=models.CASCADE)
    treatments2 = models.ForeignKey(Treatment, related_name='treatment_prescriptions2', null=True, blank=True, on_delete=models.CASCADE)
    treatments3 = models.ForeignKey(Treatment, related_name='treatment_prescriptions3', null=True, blank=True, on_delete=models.CASCADE)
    treatments4 = models.ForeignKey(Treatment, related_name='treatment_prescriptions4', null=True, blank=True, on_delete=models.CASCADE)
    treatments5 = models.ForeignKey(Treatment, related_name='treatment_prescriptions5', null=True, blank=True, on_delete=models.CASCADE)
    treatments6 = models.ForeignKey(Treatment, related_name='treatment_prescriptions6', null=True, blank=True, on_delete=models.CASCADE)
    treatments7 = models.ForeignKey(Treatment, related_name='treatment_prescriptions7', null=True, blank=True, on_delete=models.CASCADE)
    dosage_and_times = models.TextField(null=True, blank=True)
    doctor_recommendations = models.TextField(null=True, blank=True)
    next_consultation_date = models.DateTimeField()

    def __str__(self):
        return f"{self.patient.name}'s Prescription"
        