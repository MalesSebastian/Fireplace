from django.shortcuts import render
from django.shortcuts import render_to_response
from models import Post
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.db import models

def submit(request):
    if request.method == "GET":
        post_title = request.GET.get('title')
        post_text = request.GET.get('post_text')
        #user_ses = request.user
        new_post = Post(post_title, post_text)
    return render_to_response('new_post/create_post.html')
