from django.shortcuts import render_to_response , render
from models import Post


def submit(request):
    if request.method == "POST":
        post_title = request.POST.get('title')
        post_text = request.POST.get('post_text')
        category = request.POST.get('category')
        user_ses = request.user
        new_post = Post(post_title, post_text, user_ses, category)
        new_post.save()
        return render(request, 'new_post/create_post.html')
    return render(request, 'new_post/create_post.html')

