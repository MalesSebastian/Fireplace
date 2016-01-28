from django.shortcuts import render_to_response, render
from models import Post
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User


def submit(request):

    if request.method == "POST":
        post_title = request.POST.get('title')
        post_text = request.POST.get('post_text')
        category = request.POST.get('category')
        new_post = Post.objects.create(title=post_title, post_text=post_text, submitter=request.user, category=category)
        new_post.save()
        return render_to_response(request, 'new_post/su.html')
    return render(request, 'new_post/create_post.html')





