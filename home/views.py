from django.shortcuts import render_to_response

def index(request):
    if request.user.is_authenticated():
        return render_to_response('home/Front.html')
    #else
        #alt template
# Create your views here.
