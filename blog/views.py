from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post

#
# def index(request):
#     posts = Post.objects.all().order_by('-pk') # 최신 글부터 맨 위에 배치
#
#     return render(
#         request,
#         'blog/post_list.html',
#         {
#             'posts': posts
#         }
#     )

# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/post_detail.html',
#         {
#             'post': post,
#         }
#     )

# Create your views here.
