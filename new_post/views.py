from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def submit(reqest):
    return render_to_response('new_post/create_post.html')
