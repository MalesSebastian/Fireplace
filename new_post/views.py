from django.shortcuts import render_to_response
from models import Post
import pytz
from django.utils import timezone
from django.conf import settings
from django.utils.timezone import activate

def submit(request):
    if request.method == "GET":
        post_title = request.GET.get('title')
        post_text = request.GET.get('post_text')
        category = request.GET.get('category')
        user_ses = request.user
        if post_title is not None:
            new_post = Post(post_title, post_text, user_ses,category)
            new_post.save()
    return render_to_response( 'new_post/create_post.html')
