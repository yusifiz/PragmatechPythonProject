from django.shortcuts import render
from .models import Blog
# Create your views here.
def blog(request):
    blogs = Blog.objects.all()

    return render(request,'blog.html',{'blogs' : blogs})

