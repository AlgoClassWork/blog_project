from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login


from blog.models import Post
from .forms import UserRegisterForm

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

# http://127.0.0.1:8000/create/
def post_create(request):
    return render(request, 'post_form.html')

# http://127.0.0.1:8000/register/
def register(request):
    form = UserRegisterForm()
    context = {'form' : form}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_list')

    return render(request, 'register.html', context)
