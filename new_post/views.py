from django.shortcuts import render_to_response , render
from models import Post

def submit(request):
    if request.method == "GET":
        return render(request, 'new_post/create_post.html')
    if request.method == "POST":
        post_title = request.GET.get('title')
        post_text = request.GET.get('post_text')
        category = request.GET.get('category')
        user_ses = request.user
        new_post = Post(post_title, post_text, user_ses, category)
        new_post.save()
        return render(request, 'new_post/create_post.html')
        print new_post.title

