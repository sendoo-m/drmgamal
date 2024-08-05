# Generated by Django 3.2 on 2024-08-04 21:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0006_auto_20220323_0158'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('today_date', models.DateField(auto_now_add=True, verbose_name='Today Date')),
                ('medical_history', models.TextField(blank=True, null=True)),
                ('complaint', models.TextField(blank=True, null=True)),
                ('diagnosis', models.TextField(blank=True, null=True)),
                ('temp', models.CharField(blank=True, max_length=250, null=True)),
                ('weight', models.FloatField(blank=True, null=True)),
                ('doctor_notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_number', models.IntegerField(auto_created=True, verbose_name='File Number')),
                ('name', models.CharField(blank=True, max_length=250, verbose_name='Name')),
                ('occupation', models.CharField(blank=True, max_length=250, verbose_name='Occupation')),
                ('age', models.IntegerField()),
                ('birthdate', models.DateField(blank=True, verbose_name='Birth Date')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=10)),
                ('mobile_number', models.CharField(blank=True, max_length=20, unique=True, verbose_name='Phone Number')),
            ],
            options={
                'verbose_name': 'registration',
                'verbose_name_plural': 'registrations',
            },
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treatment', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('company', models.CharField(blank=True, max_length=250, null=True)),
                ('dosage', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentPrescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dosage_and_times', models.TextField(blank=True, null=True)),
                ('doctor_recommendations', models.TextField(blank=True, null=True)),
                ('next_consultation_date', models.DateTimeField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient')),
                ('treatments1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treatment_prescriptions', to='patient.treatment')),
                ('treatments2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treatment_prescriptions2', to='patient.treatment')),
                ('treatments3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treatment_prescriptions3', to='patient.treatment')),
                ('treatments4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treatment_prescriptions4', to='patient.treatment')),
                ('treatments5', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treatment_prescriptions5', to='patient.treatment')),
                ('treatments6', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treatment_prescriptions6', to='patient.treatment')),
                ('treatments7', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='treatment_prescriptions7', to='patient.treatment')),
            ],
        ),
        migrations.DeleteModel(
            name='Add_patient',
        ),
        migrations.RemoveField(
            model_name='rosheta',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='Cashf',
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='Rosheta',
        ),
        migrations.AddField(
            model_name='diseaseinfo',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='patient.patient'),
        ),
        migrations.AddField(
            model_name='diseaseinfo',
            name='treatments1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Treatments_Needs', to='patient.treatment'),
        ),
        migrations.AddField(
            model_name='diseaseinfo',
            name='treatments2',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Treatments_Needs2', to='patient.treatment'),
        ),
        migrations.AddField(
            model_name='diseaseinfo',
            name='treatments3',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Treatments_Needs3', to='patient.treatment'),
        ),
        migrations.AddField(
            model_name='diseaseinfo',
            name='treatments4',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Treatments_Needs4', to='patient.treatment'),
        ),
        migrations.AddField(
            model_name='diseaseinfo',
            name='treatments5',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Treatments_Needs5', to='patient.treatment'),
        ),
        migrations.AddField(
            model_name='diseaseinfo',
            name='treatments6',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Treatments_Needs6', to='patient.treatment'),
        ),
        migrations.AddField(
            model_name='diseaseinfo',
            name='treatments7',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Treatments_Needs7', to='patient.treatment'),
        ),
    ]
