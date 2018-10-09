from django.shortcuts import render
from .models import Blog

# Create your views here.
def allblogs(request):
    return render(request, 'blog/allblogs.html', {'blogs': Blog.objects})