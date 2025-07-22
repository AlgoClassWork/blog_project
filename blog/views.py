from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login



from blog.models import Post
from .forms import PostForm, UserRegisterForm

# Create your views here.
# http://127.0.0.1:8000/
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    context = {'posts' : posts}
    return render(request, 'post_list.html', context )

# http://127.0.0.1:8000/detail/3
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context = {'post' : post}
    return render(request, 'post_detail.html', context )

# http://127.0.0.1:8000/create/
@login_required
def post_create(request):
    form = PostForm()
    context = {'form' : form}
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', id=post.id)

    return render(request, 'post_form.html', context)

# http://127.0.0.1:8000/update/5
@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    form = PostForm(instance=post)
    context = {'form' : form}

    if post.author != request.user:
        return redirect('post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)

    return render(request, 'post_form.html', context)

# http://127.0.0.1:8000/delete/10
@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return redirect('post_list')
    
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')

    return render(request, 'post_delete.html')

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
