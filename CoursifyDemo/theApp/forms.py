from django import forms
from django.contrib.auth.models import User
from theApp.models import ClarifyDoubtModel

class StudentRegistrationModelForm(forms.ModelForm):

    password = forms.CharField(widget = forms.PasswordInput)

    class Meta():

        model = User

        fields = ('first_name','last_name','username','email','password')
