from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.template import loader, RequestContext
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect


def login(request):
    template = loader.get_template('authen/login.html')
    #return HttpResponse(template.render())

def register(request):
     if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('authen/index.html')
     else:
        form = UserForm()

     return render(request, 'authen/register.html', {'form': form})