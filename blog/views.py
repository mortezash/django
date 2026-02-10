from django.shortcuts import render, get_object_or_404
from .models import Post

def home(request):
    context = {
        'name': 'Python',
        'age': 30,
        'skills' : ['Python', 'Django', 'Docker']
    }
    return render(request, 'blog/home.html', context)

def blogs(request):
    posts = Post.objects.all().order_by('-created_at')[:10]
    return render(request, 'blog/blogs.html', {'posts': posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})