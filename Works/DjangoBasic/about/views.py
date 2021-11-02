from django.shortcuts import render

from about.models import About

# Create your views here.

def about(request):
    abouts = About.objects.all()
    return render(request,'about.html',{'abouts':abouts})