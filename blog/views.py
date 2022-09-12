from django.shortcuts import render
from .models import Post

def index(request):
    posts = Post.objects.all().order_by('-pk') # 최신 글부터 맨 위에 배치

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts
        }
    )

# Create your views here.
