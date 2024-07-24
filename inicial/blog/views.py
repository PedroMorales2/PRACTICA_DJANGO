from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.http import JsonResponse
# Create your views here.

def index(request):
    form = PostForm()
    return render(request, 'blog/index.html', {
        'forma': form,
        
    })
 


def insert_post(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.POST.get('image')
        
        #insertar en la base de datos
        new_post = Post(title=title, content=content, image=image, user=id)
        new_post.save()
        return render(request, 'blog/index.html')
    return render(request, 'blog/index.html')

