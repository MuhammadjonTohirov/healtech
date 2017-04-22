from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.views import logout
from django.shortcuts import render, redirect

from HealTech.models import SuggestionsForAppointment
from HealUsers.models import Patient, Doctor

context = {
    "user": 'anonymous',
}


# Create your views here.
def register_user(request):
    if request.method == "POST":
        f_name = request.POST.get("first_name")
        l_name = request.POST.get("last_name")
        u_name = request.POST.get("username")
        email = request.POST.get("email1")
        pwd = request.POST.get("password")
        usr = User.objects.create(username=u_name, first_name=f_name, last_name=l_name, email=email, password=pwd)
        Patient.objects.create(user=usr)
        login(request, usr)
        return render(request, "index.html", context)
    return render(request, "Auth/register.html", context)


def login_page(request):
    if request.method == "POST":
        try:
            em = request.POST.get("username")
            ps = request.POST.get("password")
            # next = request.REQUEST.get("next")
            print(em)
            print(ps)
            ur = User.objects.get(username=em)
            pat = Patient.objects.get(user=ur)
            login(request, ur)
            return redirect(to='profile')
        except:
            context["error"] = "User is not exist, try again"
            return render(request, "Auth/login.html", context)
    context["error"] = ""
    return render(request, "Auth/login.html", context)


def log_out(request):
    if not request.user.is_anonymous:
        logout(request)
        return render(request, "Auth/login.html", context)
    return render(request, "index.html", context)


def fill_profile(request):
    if not request.user.is_anonymous:
        try:
            if request.method == "POST":
                bdate = request.method.POST.get("birth_date")
                about = request.method.POST.get("about")
                avatar = request.method.POST.get("image")
                Patient.objects.create(user=request.user, birth_date=bdate, image=avatar, about_illness=about)
                return render(request, "Profile/fill_profile.html")
            return render(request, "Profile/fill_profile.html")
        except:
            return render(request, "index.html")


@login_required
def profile(request):
    context["user"] = request.user
    usr = request.user.id
    patient = Patient.objects.get(user_id=usr)
    print(patient.user.username)
    context["user"] = patient
    context["img_url"] = patient.image.url
    context["appointments"] = SuggestionsForAppointment.objects.filter(
        suggestion_for__from_patient__user_id=usr)
    return render(request, "Profile/profile.html", context)


def doc_profile(request, doc_id):
    if not request.user.is_anonymous:
        doctor = Doctor.objects.get(user_id=doc_id)
        context["doctor"] = doctor
        return render(request, "Profile/profile_doctor.html", context)
    return render(request, 'index.html')
