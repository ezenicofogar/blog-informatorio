from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    # Forum
    path('', views.ForumListView.as_view(), name='forum_list'),
    path('forum/<slug:forum>/', views.ForumDetailView.as_view(), name='forum_detail'),

    # Post
    path('forum/<slug:forum>/post/<slug:post>/',
         views.PostDetailView.as_view(), name='post_detail'),

    # Comment
    path('forum/<slug:forum>/post/<slug:post>/createcomment/',
         views.PostCommentCreateView.as_view(), name='comment_create'),
    path('editcomment/<int:pk>/',
         views.PostCommentUpdateView.as_view(), name='comment_update'),
    path('deletecomment/<int:pk>/',
         views.PostCommentDeleteView.as_view(), name='comment_delete'),
]
