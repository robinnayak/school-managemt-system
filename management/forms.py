from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from management.models import *

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','roll_number','courses','section']
        widgets = {
            'courses': forms.CheckboxSelectMultiple
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name','teacher','description']
        widgets = {
            'teacher':forms.CheckboxInput
        }

