from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, Category
from django.core.paginator import Paginator

# Create your views here.
def community(request):
  page = request.GET.get('page', '1')
  posts = Post.objects.all().order_by('-created_at')
  category = Category.objects.all()
  paginator = Paginator(posts, 20)
  page_obj = paginator.get_page(page)

  context = {
    'posts': page_obj,
    'category': category,
  }

  return render(request, 'community/community.html', context)

@login_required
def community_create(request):

  posts = Post.objects.all().order_by('-created_at')
  category = Category.objects.all()

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
    'category': category,
    'form': form,
  }

  return render(request, 'community/community_create.html', context)

def detail(request, category_id, pk):
  post = get_object_or_404(Post, pk=pk)
  category = Category.objects.all()

  post.increase_views()
  
  return render(request, 'community/detail.html', {'post': post, 'category': category})

def category(request, category_id):
  page = request.GET.get('page', '1')
  category = get_object_or_404(Category, id=category_id)
  posts = Post.objects.filter(category=category)
  categories = Category.objects.all()
  paginator = Paginator(posts, 20)
  page_obj = paginator.get_page(page)

  context = {
    'category': category,
    'posts': page_obj,
    'categories': categories,
  }
  
  return render(request, 'community/category.html', context)

def like_post(request, category_id, pk):
  post = get_object_or_404(Post, pk=pk)

  if request.user.is_authenticated:
    if request.user in post.likes.all():
      post.likes.remove(request.user)
    else:
      post.likes.add(request.user)

  return redirect('community:detail', category_id=post.category.pk, pk=pk)