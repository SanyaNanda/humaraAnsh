from django.contrib import admin

from .models import Contact, User, Patient, Doctor

admin.site.register(User)
admin.site.register(Patient)
admin.site.register(Doctor)
admin.site.register(Contact)

