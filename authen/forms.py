from django.contrib.auth.models import User
#from django.forms import ModelForm
from django import  forms

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        #widgets = {
            #'username': forms.TextInput(attrs={'class': 'inputText'}),
           # 'email': forms.TextInput(attrs={'class': 'inputText'}),
            #'password': forms.TextInput(attrs={'class': 'inputText'}),

# class Userlogin(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ('username', 'password')
