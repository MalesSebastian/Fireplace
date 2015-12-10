from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.template import loader
from models import Account


def app_login(request):
    if request.method == 'GET':
        return render(request, "authen/login.html")
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/submit')
            else:
                print "Disabled account"
        else:
            print "Invalid data"
    return render(request, 'authen/login.html')


def index(request):
    template = loader.get_template('authen/index.html')
    return HttpResponse(template.render())


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        new_user = User.objects.create_user(username, email, password)
        new_user.save()
        account = Account.objects.create(user=new_user)
        account.save()
    #    login(request, new_user)
        return HttpResponseRedirect('/index')
    return render(request, 'authen/register.html')

