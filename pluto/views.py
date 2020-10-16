from django.shortcuts import render

def all_blog(request):
    return render(request, 'pluto/all_blog.html')
