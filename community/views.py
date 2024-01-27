from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm

# Create your views here.
def community(request):
  return render(request, 'community/community.html')

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