from django.db import models

# Create your models here.
category = {
  ("general", "자유게시판"),
  ("qnA", "질문게시판"),
  ("wisesayings", "명언/좋은글귀"),
  ("family", "가족"),
  ("health", "건강/운동"),
  ("marry", "결혼/부부"),
  ("money", "금전/재테크"),
  ("diet", "다이어트/외모"),
  ("relationship", "대인관계"),
  ("pet", "반려 동식물"),
  ("life", "삶/죽음"),
  ("gender", "성"),
  ("travel", "여행"),
  ("love", "연애/사랑"),
  ("recipe", "요리/식단"),
  ("religion", "종교"),
  ("hobby", "취미"),
  ("career", "취업/진로"),
  ("friend", "친구/우정"),
  ("mind", "정신건강"),
  ("mbti", "MBTI"),
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