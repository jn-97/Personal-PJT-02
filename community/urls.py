from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('', views.community, name="community"),
    path('community_create/', views.community_create, name="community_create"),
    path('<int:pk>/', views.detail, name="detail"),
]
