from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import PostForm
from .models import Post, Category, Comment
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
def community(request):
  page = request.GET.get('page', '1')
  posts = Post.objects.all().order_by('-created_at')
  category = Category.objects.all()
  paginator = Paginator(posts, 20)
  page_obj = paginator.get_page(page)
  # 스크랩
  if request.user.is_authenticated:
    bookmarked_posts_count = request.user.bookmarks.count()
  else:
    bookmarked_posts_count = 0

  context = {
    'posts': page_obj,
    'category': category,
    'bookmarked_posts_count': bookmarked_posts_count,
  }

  return render(request, 'community/community.html', context)

def coolitems(request):
  return render(request, 'community/coolitems.html')

def fabric(request):
  return render(request, 'community/fabric.html')

@login_required
def community_create(request):

  posts = Post.objects.all().order_by('-created_at')
  category = Category.objects.all()
  # 스크랩
  if request.user.is_authenticated:
    bookmarked_posts_count = request.user.bookmarks.count()
  else:
    bookmarked_posts_count = 0

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
    'bookmarked_posts_count': bookmarked_posts_count,
  }

  return render(request, 'community/community_create.html', context)

def detail(request, category_id, pk):
  post = get_object_or_404(Post, pk=pk)
  category = Category.objects.all()
  # 스크랩
  if request.user.is_authenticated:
    bookmarked_posts_count = request.user.bookmarks.count()
  else:
    bookmarked_posts_count = 0

  post.increase_views()

  context = {
    'post': post,
    'category': category,
    'bookmarked_posts_count': bookmarked_posts_count,
  }

  
  return render(request, 'community/detail.html', context)

@login_required
def update(request, category_id, pk):
  posts = get_object_or_404(Post, pk=pk)
  category = Category.objects.all()
  # 스크랩
  if request.user.is_authenticated:
    bookmarked_posts_count = request.user.bookmarks.count()
  else:
    bookmarked_posts_count = 0

  # 게시물 작성자만 수정할 수 있도록 권한을 확인합니다.
  if posts.writer != request.user:
    return redirect('community:detail', category_id=posts.category.pk, pk=pk)

  if request.method == 'POST':
    form = PostForm(request.POST, instance=posts)
    if form.is_valid():
      form.save()
      return redirect('community:detail', category_id=posts.category.pk, pk=pk)
  else:
    form = PostForm(instance=posts)

  context = {
    'posts': posts,
    'category': category,
    'form': form,
    'bookmarked_posts_count': bookmarked_posts_count,
  }

  return render(request, 'community/update.html', context)

def delete(request, category_id, pk):
  # 삭제할 게시물 객체를 가져옵니다.
  post = get_object_or_404(Post, pk=pk)
  category = Category.objects.all()

  # 사용자가 작성한 게시물인지 확인합니다.
  if post.writer != request.user:
    # 작성자가 아닌 경우, 상세 페이지로 리다이렉트합니다.
    return redirect('community:detail', category_id=category_id, pk=pk)

  # 게시물을 삭제합니다.
  post.delete()

  # 게시물 목록 페이지로 리다이렉트합니다.
  return redirect('community:community')

def category(request, category_id):
  page = request.GET.get('page', '1')
  category = get_object_or_404(Category, id=category_id)
  posts = Post.objects.filter(category=category)
  categories = Category.objects.all()
  paginator = Paginator(posts, 20)
  page_obj = paginator.get_page(page)
  # 스크랩
  if request.user.is_authenticated:
    bookmarked_posts_count = request.user.bookmarks.count()
  else:
    bookmarked_posts_count = 0

  context = {
    'category': category,
    'posts': page_obj,
    'categories': categories,
    'bookmarked_posts_count': bookmarked_posts_count,
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

def add_comment(request, category_id, pk):
  post = get_object_or_404(Post, pk=pk)
  
  if request.method == 'POST':
    content = request.POST.get('content')
      
    if content:
      comment = Comment.objects.create(user=request.user, post=post, content=content)
  return redirect('community:detail', category_id=category_id, pk=pk) 

def delete_comment(request, category_id, pk, comment_id):
  comment = get_object_or_404(Comment, pk=comment_id)  
  comment.delete()

  return redirect('community:detail', category_id=category_id, pk=pk)

@login_required
def toggle_bookmark(request, post_id):
  post = get_object_or_404(Post, pk=post_id)
  
  # 사용자가 현재 게시물을 북마크한 경우 북마크를 제거하고, 아닌 경우 북마크를 추가합니다.
  if post in request.user.bookmarks.all():
    request.user.bookmarks.remove(post)
    bookmarked = False
  else:
    request.user.bookmarks.add(post)
    bookmarked = True

  # Ajax 요청에 대한 응답
  if request.is_ajax():
    return JsonResponse({'bookmarked': bookmarked})
  else:
    # 비동기 요청이 아닌 경우, 해당 게시물의 상세 페이지로 리다이렉트합니다.
    return redirect('community:detail', category_id=post.category.pk, pk=post_id)