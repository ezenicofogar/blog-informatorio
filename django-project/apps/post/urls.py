from django.urls import path
from apps.post import views as view

app_name = 'post'

urlpatterns = [
    path('post/<slug:slug>/', view.PostListView.as_view(), name='post_list'),
    path('post/<slug:slug>/', view.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/', view.PostCreateView.as_view(), name='post_create'),
    path('post/<slug:slug>/', view.PostUpdateView.as_view(), name='post_update'),
    path('post/<slug:slug>/', view.PostDeleteView.as_view(), name='post_confirm_delete'),
    path('post/<slug:slug>/', view.PostDetailView.as_view(), name='post_detail'),


]




