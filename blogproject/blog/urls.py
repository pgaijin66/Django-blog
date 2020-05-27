from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('linux/', views.linux, name='blog-linux'),
    path('security/', views.security, name='blog-security'),
    path('devops/', views.devops, name='blog-devops')
]