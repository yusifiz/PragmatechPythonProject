from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404
# Create your views here.
def blog(request):
    blogs = Blog.objects.all()

    return render(request,'blog.html',{'blogs' : blogs})

def blog_details(request,slug):
    
    blogs = get_object_or_404(Blog, slug=slug)
    return render(request, "blog-details.html",{'blogs' : blogs})