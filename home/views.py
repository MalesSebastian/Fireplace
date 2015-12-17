from django.shortcuts import render_to_response
from new_post.models import Post
from django.utils import timezone

def index(request):
    if request.user.is_authenticated():
        posts = Post.objects.filter(time__lte=timezone.now)
        return render_to_response('home/Front.html', {'posts': posts})
    #else
        #alt template
# Create your views here.
