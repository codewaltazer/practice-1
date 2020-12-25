from django.shortcuts import render
from .models import Blog

def blog(request):
    blog_all = Blog.objects.all()
    return render(request, 'blog/blog.html',{'blog_all':blog_all})
    
    
  

