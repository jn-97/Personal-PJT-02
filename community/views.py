from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, Category
from django.core.paginator import Paginator

# Create your views here.
def community(request):
  page = request.GET.get('page', '1')
  posts = Post.objects.all().order_by('-created_at')
  paginator = Paginator(posts, 20)
  page_obj = paginator.get_page(page)

  context = {
    'posts': page_obj,
  }

  return render(request, 'community/community.html', context)

@login_required
def community_create(request):

  posts = Post.objects.all().order_by('-created_at')

  if request.method == 'POST':
    form = PostForm(request.POST)

    if form.is_valid():
      form.instance.writer = request.user
      form.save()
      return redirect('community:community')
    
  else:
    form = PostForm()

  context = {
    'posts': posts,
    'form': form,
  }

  return render(request, 'community/community_create.html', context)

def detail(request, category_id, pk):
  post = get_object_or_404(Post, pk=pk)
  category = Category.objects.all().order_by('-id')
  
  return render(request, 'community/detail.html', {'post': post, 'category': category})

def category(request, category_id):
  category = get_object_or_404(Category, id=category_id)
  posts = Post.objects.filter(category=category)
  categories = Category.objects.all().order_by('-id')

  context = {
    'category': category,
    'posts': posts,
    'categories': categories,
  }
  
  return render(request, 'community/category.html', context)