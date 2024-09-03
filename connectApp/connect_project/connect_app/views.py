from django.shortcuts import render,redirect
from .models import Post
from django.core.paginator import Paginator
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')

def explore(request):
    posts_list = Post.objects.all()
    paginator = Paginator(posts_list, 5)  # Show 5 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'explore.html', {'posts': page_obj})

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user  # Use request.user to get the logged-in user
            post.save()
            return redirect('explore')  # redirect to the explore page after submission
    else:
        form = PostForm()
    
    return render(request, 'create_post.html', {'form': form})
