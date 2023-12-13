from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('community/', views.community, name="community"),
]
