from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post, Category

# CBV 방식
class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post

# # FBV 방식
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
#
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
