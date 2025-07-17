from django.shortcuts import render, get_object_or_404

from blog.models import Post

# Create your views here.
# http://127.0.0.1:8000/
def post_list(request):
    posts = Post.objects.all()
    context = {'posts' : posts}
    return render(request, 'post_list.html', context )

# http://127.0.0.1:8000/detail/3
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post' : post}
    return render(request, 'post_detail.html', context )

