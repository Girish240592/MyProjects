from django import forms
from .models import Student
class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=['name','roll','address']
        labels={'name': 'Enter Name', 'roll': 'Enter Roll Number','address':'Enter Address'}
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Please enter Your Name'}),
            'roll': forms.TextInput(attrs={'placeholder': 'Please enter Your Roll Number'}),
            'address': forms.Textarea(attrs={'placeholder': 'Please enter Your Address'}),
        }
        
        