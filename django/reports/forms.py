from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'doctor', 'patient','body','file')
		

		widgets = {
			'title':forms.TextInput(attrs={'class':'form-control','placeholder': 'Title'}),
			'doctor':forms.TextInput(attrs={'class':'form-control','value':'', 'id':'sanya', 'type':'hidden'}),
			'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Details'}),
        }