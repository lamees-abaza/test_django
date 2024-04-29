from django.shortcuts import get_object_or_404, render
from .models import Post 
from django.http import Http404

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post/list.html',{'posts': posts})


def post_detail(request,id):
    # method 1

    # try:
    #     post = Post.objects.all(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No Post Found.")    
    # return render(request, 'blog/post/list.html',{'post': post})

    # method 2
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    return render(request, 'blog/post/detail.html',{'post': post})
















