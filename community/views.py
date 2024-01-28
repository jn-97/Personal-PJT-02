from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.
def community(request):
  page = request.GET.get('page', '1')
  posts = Post.objects.all().order_by('-created_at')
  paginator = Paginator(posts, 20)
  page_obj = paginator.get_page(page)

  context = {
    'posts': page_obj
  }

  return render(request, 'community/community.html', context)

@login_required
def community_create(request):
  if request.method == 'POST':
    form = PostForm(request.POST)

    if form.is_valid():
      form.instance.writer = request.user
      form.save()
      return redirect('community:community')
    
  else:
    form = PostForm()

  return render(request, 'community/community_create.html', {'form': form})