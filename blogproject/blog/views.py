from django.shortcuts import render
from django.http import HttpResponse
from .models import BlogPost

# Create your views here.
def home(request):
   context = {
       'posts' : BlogPost.objects.all()
   } 
   return render(request, 'blog/home.html', context)

def about(request):
    # return HttpResponse('<h2>about</h2>')
    return render(request, 'blog/about.html', {'title':'About'})

def linux(request):
    return render(request, 'blog/linux.html', {'title':'Linux'})

def security(request):
    return render(request, 'blog/security.html', {'title':'security'})

def devops(request):
    return render(request, 'blog/devops.html', {'title':'devops'})