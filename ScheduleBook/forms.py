from django import forms
from .models import Record
from django.utils.safestring import mark_safe



CHOICES=[('Yes','Yes'),
         ('No','No')]


class RecordCreateForm(forms.ModelForm):
	Exercise1 = forms.ChoiceField(choices=CHOICES,initial='Yes', widget=forms.RadioSelect(attrs={'class':'form-check form-check-inline no'}))
	ML_Course = forms.ChoiceField(choices=CHOICES,initial='Yes', widget=forms.RadioSelect(attrs={'class':'form-check form-check-inline no'}))
	ML_Project = forms.ChoiceField(choices=CHOICES,initial='Yes', widget=forms.RadioSelect(attrs={'class':'form-check form-check-inline no'}))
	Exercise2 = forms.ChoiceField(choices=CHOICES,initial='Yes', widget=forms.RadioSelect(attrs={'class':'form-check form-check-inline no'}))
	DSA_Learning = forms.ChoiceField(choices=CHOICES,initial='Yes', widget=forms.RadioSelect(attrs={'class':'form-check form-check-inline no'}))
	DSA_Coding = forms.ChoiceField(choices=CHOICES,initial='Yes', widget=forms.RadioSelect(attrs={'class':'form-check form-check-inline no'}))
	Walk = forms.ChoiceField(choices=CHOICES, initial='Yes',widget=forms.RadioSelect(attrs={'class':'form-check form-check-inline no'}))
	Problem_Solving = forms.ChoiceField(choices=CHOICES, initial='Yes',widget=forms.RadioSelect(attrs={'class':'form-check form-check-inline no'}))
	class Meta:
		model = Record
		fields = ['Exercise1','ML_Course','ML_Project','Exercise2','DSA_Learning','DSA_Coding','Walk','Problem_Solving']

