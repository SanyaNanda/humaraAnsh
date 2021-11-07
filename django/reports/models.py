from django.db import models
from django.contrib.auth.models import User
from portal.models import Doctor, Patient
from django.urls import reverse


class Post(models.Model):
	title = models.CharField(max_length=255)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reciever', default=None)
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True, editable=False)
	file = models.FileField()

	# def get_absolute_url(self):
	# 	return reverse('home')

class Prescriptions(models.Model):
	title = models.CharField(max_length=255)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reciever_pres', default=None)
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True, editable=False)

	# def get_absolute_url(self):
	# 	return reverse('home')

# class Choice(models.Model):
#     selected_by = models.ManyToManyField(Patient, related_name='choose_doctor')
    
#     def total_patients(self):
#         return self.selected_by.count()
    
#     def selectors(self):
#         return self.selected_by.all()