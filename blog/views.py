from django.shortcuts import render , get_list_or_404
from .models import Blog

def blog(request):
    blog_all = Blog.objects.all()
    return render(request, 'blog/blog.html',{'blog_all':blog_all})

def detail(request, blog_id):
    id_blog = get_list_or_404(Blog, pk=blog_id)

    return render(request, 'blog/detail.html', {'id_blog':id_blog})
    
    
  

