from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
category = {
  ("General", "자유게시판"),
  ("QnA", "질문게시판"),
}

class Post(models.Model):
  writer = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
  category = models.CharField(max_length=20, choices=category, default="general")
  title = models.CharField(max_length=100)
  contents = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.title