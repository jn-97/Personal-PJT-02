from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=20)

  def __str__(self):
    return self.name

class Post(models.Model):
  writer = models.ForeignKey('accounts.User', on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
  title = models.CharField(max_length=100)
  contents = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  views = models.IntegerField(default=0) # 조회수

  def __str__(self):
    return self.title
  
  def increase_views(self):
    self.views += 1
    self.save()