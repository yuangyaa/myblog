#from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Post

def index(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blog/index.html', {'posts': posts})

def detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'blog/detail.html', {'post': post})

