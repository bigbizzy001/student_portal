from django.contrib.auth.models import User
from django import forms

from .models import LecturerProfile

class LecturerRegistrationForm(forms.ModelForm):

    password = forms.CharField(max_length=20, label='Password', widget=forms.PasswordInput)
    repeat_password = forms.CharField(max_length=20, label='Repeat Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

        widgets = {
            'password': forms.PasswordInput(attrs={
                'placeholder': 'Enter Password'
            }),
            'repeat_password': forms.PasswordInput(attrs={
                'placeholder': 'Enter Password again'
            }),
        }

    def clean_repeat_password(self):
        cd = self.cleaned_data
        if cd['password'] != cd['repeat_password']:
            raise forms.ValidationError("Passwords don't match")
        return cd['repeat_password']


class LecturerProfileEditForm(forms.ModelForm):

    class Meta:
        model = LecturerProfile
        fields = ['title', 'name', 'qualification', 'designation', 'field_of_specialization', 'course_taught']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']
