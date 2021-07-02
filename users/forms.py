from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    phone_number = forms.IntegerField()
    # profile_pic = forms.ImageField()
    class Meta:
        model = User
        fields = ('username','email','password1','password2','phone_number')
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
