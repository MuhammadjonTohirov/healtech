# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-22 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HealUsers', '0002_auto_20170421_1952'),
        ('HealTech', '0002_auto_20170421_1952'),
    ]

    operations = [
        migrations.CreateModel(
            name='SuggestionsForAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=2048)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('drugs', models.ManyToManyField(related_name='drugs', to='HealTech.Drug')),
                ('illness', models.ManyToManyField(blank=True, related_name='patient_illness', to='HealUsers.TypeOfIllness', verbose_name='illnesses')),
            ],
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='illness',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='suggested_drugs',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='for_doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_user', to='HealUsers.Doctor'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='from_patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_user', to='HealUsers.Patient'),
        ),
        migrations.AddField(
            model_name='suggestionsforappointment',
            name='suggestion_for',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to='HealTech.Appointment'),
        ),
    ]