from django.shortcuts import render

# Create your views here.
# http://127.0.0.1:8000/
def post_list(request):
    return render(request, 'post_list.html')
