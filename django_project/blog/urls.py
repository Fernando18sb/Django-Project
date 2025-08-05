from django.urls import path
from .views import (PostListView,
                    PostDetailView,
                    PostCreateView)
from . import views

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='about'),
]
