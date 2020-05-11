from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    blogs = Blog.objects.order_by('-whencreated')
    return render(request,'all_blogs.html',{'blogs':blogs})

def specific_blog(request,blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request,'specific_blog.html',{'blog':blog}) 