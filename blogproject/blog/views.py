from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author':'Prabesh Thapa',
        'title':'Blog post 1',
        'Content':'Content 1',
        'date_posted':'May 22, 2020'
     },
     {
        'author':'Prabesh Thapa',
        'title':'Blog post 2',
        'Content':'Content 2',
        'date_posted':'May 22, 2020'
    }

]

# Create your views here.
def home(request):
   context = {
       'posts':posts
   } 
    # return HttpResponse('<h1>Blog Home</h1>')
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
