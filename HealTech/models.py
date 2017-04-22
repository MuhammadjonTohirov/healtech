from django.contrib.contenttypes.models import ContentType
from django.db import models

from HealUsers.models import Doctor, Patient, TypeOfIllness


class Drug(models.Model):
    title = models.CharField(max_length=255, help_text="ex: trimol")
    description = models.TextField(max_length=2048, help_text="ex: for headache")
    for_illness = models.ManyToManyField(TypeOfIllness, help_text="select types", verbose_name='illnesses',
                                         related_name='drug_illness',
                                         blank=False)

    def __str__(self):
        return self.title


class Appointment(models.Model):
    for_doctor = models.ForeignKey(Doctor, related_name='doctor_user')
    from_patient = models.ForeignKey(Patient, related_name='patient_user')
    # illness = models.ManyToManyField(TypeOfIllness, verbose_name='illnesses', related_name='patient_illness',
    #                                  blank=True)
    # suggested_drugs = models.ManyToManyField(Drug, related_name="appointment_suggestion")
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    posted_at = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return self.from_patient.user.first_name + " from " + self.for_doctor.user.first_name + " " + str(
            self.date) + " " + str(self.time)


class SuggestionsForAppointment(models.Model):
    suggestion_for = models.ForeignKey(Appointment, related_name='patient')
    illness = models.ManyToManyField(TypeOfIllness, verbose_name='illnesses', related_name='patient_illness',
                                     blank=True)
    drugs = models.ManyToManyField(Drug, related_name='drugs')
    description = models.TextField(max_length=2048)
    date = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.suggestion_for.from_patient.user.first_name + " " + str(self.date)
