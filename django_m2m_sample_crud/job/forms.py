from django import forms
from .models import Job

class JobForm(forms.ModelForm): 
	class Meta:
		model = Job
		widgets = {
			'title': forms.TextInput(attrs={"class":"required form-control pull-left", "style":"width:800px"}),
			'description': forms.Textarea(attrs={"class":"required form-control pull-left", "style":"width:800px"}),
		}