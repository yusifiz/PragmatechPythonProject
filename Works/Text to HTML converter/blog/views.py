from typing_extensions import ParamSpec
from django.shortcuts import render
from .models import Post
from .forms import Post, PostForm
# Create your views here.

def home(request):
    form=PostForm()
    return render(request, 'blog/home.html',{'form':form})