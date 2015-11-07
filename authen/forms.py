from django.contrib.auth.models import User
#from django.forms import ModelForm
from django import  forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'testcss'}),
            'email': forms.TextInput(attrs={'class': 'create_acount'}),
            'password': forms.TextInput(attrs={'class': 'create_acount'})
        }