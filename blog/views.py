from django.shortcuts import render

from blog.models import Post

# Create your views here.
# http://127.0.0.1:8000/
def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'post_list.html', context )