from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community, name="community"),
    path('community_create/', views.community_create, name="community_create"),
    path('<int:category_id>/', views.category, name="category"),
    path('<int:category_id>/<int:pk>/', views.detail, name="detail"),
    path('<int:category_id>/<int:pk>/update/', views.update, name="update"),
    path('<int:category_id>/<int:pk>/delete/', views.delete, name="delete"),
    path('<int:category_id>/<int:pk>/like/', views.like_post, name="like_post"), # 좋아요
    path('<int:category_id>/<int:pk>/comment/', views.add_comment, name="add_comment"), # 댓글
    path('<int:category_id>/<int:pk>/comment/<int:comment_id>/delete/', views.delete_comment, name="delete_comment"), # 댓글 삭제
    path('toggle_bookmark/<int:post_id>/', views.toggle_bookmark, name='toggle_bookmark'),
]
