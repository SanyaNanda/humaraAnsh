from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.fields import CharField, EmailField, FloatField, IntegerField
from django.utils.html import escape, mark_safe

class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    pregnancy_month = IntegerField(default=None,null=True)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    specialist = CharField(max_length=255)
    hospital = CharField(max_length=255)
    experience_years = FloatField(null=True)

class Contact(models.Model):
    name = CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.email

    
