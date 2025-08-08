from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    PasswordReset,
    PasswordResetDone,
    PasswordResetConfirm,
    PasswordResetComplete

)
from . import views

urlpatterns = [
    path('blog/', PostListView.as_view(), name='blog'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('about/', views.about, name='about'),
    path(
        'password-reset/done/',
         PasswordResetDone.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'
    ),
    path(
        'password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirm.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'
    ),
    path(
        'password-reset/',
         PasswordReset.as_view(
             template_name='users/password_reset.html'
         ),
         name='password_reset'
    ),
    path(
        'password-reset-complete/',
         PasswordResetComplete.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'
    ),
]
