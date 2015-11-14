from django.shortcuts import render
from django.contrib.auth.models import User
from forms import UserForm
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.template import loader
from django.utils.datastructures import MultiValueDictKeyError

def login(request):
    try:
        username = request.POST.get['username']
    except:
        username = False
    try:
        password = request.POST.get['password']
    except:
        password = False
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/index2')
        else:
            print "Disabled account"
    else:
        print "Invalid data"
    return render(request, 'authen/login.html')
def index2(request):
    template = loader.get_template('authen/index.html')
    return  HttpResponse(template.render())

def index(request):
    template = loader.get_template('authen/index.html')
    return  HttpResponse(template.render())
def register(request):
     if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(new_user)
            # redirect, or however you want to get to the main view
            return HttpResponseRedirect('/index')
     else:
        form = UserForm()

     return render(request, 'authen/register.html', {'form': form})

