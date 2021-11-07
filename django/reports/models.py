from django.db import models
from django.contrib.auth.models import User
from django.portal.models import Doctor, Patient
from django.urls import reverse

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reciever', default=None)
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True, editable=False)
	file = models.FileField()

	def get_absolute_url(self):
		return reverse('home')

class Prescriptions(models.Model):
	title = models.CharField(max_length=255)
	doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='reciever_pres', default=None)
	body = models.TextField()
	post_date = models.DateTimeField(auto_now_add=True, editable=False)

	def get_absolute_url(self):
		return reverse('home')