from django.shortcuts import render_to_response
from django.db import models
from new_post.models import Post

def index(request):
    if request.user.is_authenticated():
        posts = posts.object.all()
        return render_to_response('home/Front.html', {'posts': posts})
    #else
        #alt template
# Create your views here.
