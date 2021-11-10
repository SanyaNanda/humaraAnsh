from django import forms
from django.core.exceptions import ValidationError
from portal.models import Patient
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'doctor', 'patient','body','file')
		

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Title'}),
			'doctor':forms.TextInput(attrs={'class':'form-control','value':'', 'id':'sanya', 'type':'hidden'}),
			'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Details'}),
			# 'patient':forms.ChoiceField(attrs={}),
        }

	# def clean(self):
	# 	patient = self.cleaned_data.get('patient')
	# 	doctor = self.cleaned_data.get('doctor')
	# 	if patient.choice == doctor.user.id:
	# 		return patient
	# 	else:
	# 		raise ValidationError('patient not mapped to doctor {} {}'.format(patient.choice, doctor.user.id))

