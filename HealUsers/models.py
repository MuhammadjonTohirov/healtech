from django.contrib.auth.models import User
from django.db import models


class JobType(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)

    def __str__(self):
        return self.title


class CategoryOfDocs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=2048)

    def __str__(self):
        return self.title


class UserImage(models.Model):
    usr = models.OneToOneField(User)
    img = models.FileField(upload_to='user/image')

    def __str__(self):
        return self.usr.get_full_name()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_user')
    address = models.CharField(max_length=1024, default="home, Street, City, District, Country")
    # room_number = models.OneToOneField(Room1, on_delete=models.CASCADE, related_name='doctor_room_number')
    birth_date = models.DateField(auto_now=False)
    pos = models.ManyToManyField(CategoryOfDocs, related_name='doctor_position')
    validation = ['.jpg', '.png']
    image = models.FileField(upload_to='doctors/image')
    description = models.TextField(max_length=1024, blank=True)
    works_from = models.TimeField(blank=False)
    works_to = models.TimeField(blank=False)

    def __str__(self):
        return self.user.username


class TypeOfIllness(models.Model):
    title = models.CharField(max_length=255, help_text="ex: Tuberculosis", blank=False, null=False)
    validation = ['*.jpg', '*.png']
    image = models.FileField(upload_to='Illness/image', blank=True, validators=validation,
                             help_text="select images like *.jpg, *.png")
    description = models.TextField(max_length=2048, blank=False, null=False)

    def __str__(self):
        return self.title


class Patient(models.Model):
    validation = ['*.jpg', '*.png']
    user = models.OneToOneField(User, related_name='patient_user')
    image = models.FileField(upload_to='patients/image', help_text="select images like *.jpg, *.png", blank=True)
    phone_number = models.CharField(max_length=13, help_text="ex: +998935741369", blank=True)
    birth_date = models.DateField(auto_now=False, blank=True)
    about_illness = models.TextField(max_length=1024, blank=True)
    registered = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now=True)

    # def create_user(self, user, image, illness, phone_number, birht_date, about):
    def __str__(self):
        return self.user.first_name

    def create_user_img(self):
        UserImage.objects.create(usr=self.user, image=self.image)
