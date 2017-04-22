from django.shortcuts import render

from HealTech.models import Appointment
from HealUsers.models import Doctor, Patient


def index(request):
    return render(request, "index.html")


def contact_us(request):
    return render(request, "Contacts\page-contact.html")


def make_an_appointment(request, doc_id):
    context = {
        "id": doc_id,
    }
    if request.method == "POST":
        if not request.user.is_anonymous:
            try:
                date1 = request.POST.get("date")
                time = request.POST.get("time")
                Appointment.objects.create(for_doctor=Doctor.objects.get(id=doc_id),
                                           from_patient=Patient.objects.get(id=request.user.id), date=date1,
                                           time=time)
                context["error"] = ""
                return render(request, "Forum/appointment_successfully.html",context)
            except:
                context["error"] = "enter fields correctly, like written in example"
                return render(request, "Forum/appointment.html", context)
    context["error"] = ""
    return render(request, "Forum/appointment.html", context)
