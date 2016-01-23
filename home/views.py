from django.shortcuts import render_to_response
from new_post.models import Post


def home(request):
    if request.user.is_authenticated():
        return render_to_response('home/Front.html', {
            'posts': Post.objects.order_by('-time')
        })
    # else
        # alt template
# Create your views here.
