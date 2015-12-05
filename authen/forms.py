<<<<<<< HEAD
=======
from django.contrib.auth.models import User
#from django.forms import ModelForm
from django import  forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'createAcount inputText'}),
            'email': forms.TextInput(attrs={'class': 'createAcount inputText'}),
            'password': forms.TextInput(attrs={'class': 'createAcount inputText'}),
        }
#class Userlogin(forms.ModelForm):
    #class Meta:
     #   model = User
     #   fields = ('username', 'password')
>>>>>>> origin/sebi
