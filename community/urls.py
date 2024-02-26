from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community, name="community"),
    path('community_create/', views.community_create, name="community_create"),
    path('<int:category_id>/<int:pk>/', views.detail, name="detail"),
    path('<int:category_id>/', views.category, name="category"),
    path('<int:category_id>/<int:pk>/like/', views.like_post, name="like_post"),
]
