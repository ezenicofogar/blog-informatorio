from django.views import generic
from django.contrib.auth import mixins
from django.shortcuts import get_object_or_404
from . import models

# Create your views here.
class ForumListView(generic.ListView):
    model = models.Forum
    template_name = 'article/forum_list.html'

class ForumDetailView(generic.DetailView):
    model = models.Forum
    template_name = 'article/forum_detail.html'
    def get_object(self):
        forum_slug = self.kwargs.get('forum')
        forum = get_object_or_404(self.get_queryset(), slug=forum_slug)
        return forum

class PostDetailView(generic.DetailView):
    model = models.Post
    template_name = 'article/post_detail.html'
    def get_object(self):
        forum_slug = self.kwargs.get('forum')
        post_slug = self.kwargs.get('post')
        post = get_object_or_404(self.get_queryset(), slug=post_slug, forum__slug=forum_slug)
        return post

class PostCommentCreateView(mixins.LoginRequiredMixin, generic.CreateView):
    model = models.Comment
    fields = ['body']

    def form_valid(self, form):
        form.instance.author = self.request.user

        forum_slug = self.kwargs.get('forum')
        post_slug = self.kwargs.get('post')
        post = get_object_or_404(models.Post, slug=post_slug, forum__slug=forum_slug)

        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
        from django.urls import reverse_lazy
        forum_slug = self.kwargs.get('forum')
        post_slug = self.kwargs.get('post')
        return reverse_lazy('article:post_detail', kwargs={'forum':forum_slug, 'post':post_slug})

class PostCommentUpdateView(mixins.UserPassesTestMixin, generic.UpdateView):
    model = models.Comment
    fields = ['body']
    
    def test_func(self):
        user = self.request.user
        if user.has_perm("article.change_comment"):
            return True
        obj = self.get_object()
        if obj.author == user:
            return True
        return False

    def get_success_url(self):
        from django.urls import reverse_lazy
        obj = self.get_object()
        forum_slug = obj.post.forum.slug
        post_slug = obj.post.slug
        return reverse_lazy('article:post_detail', kwargs={'forum':forum_slug, 'post':post_slug})

class PostCommentDeleteView(mixins.UserPassesTestMixin, generic.DeleteView):
    model = models.Comment
    
    def test_func(self):
        user = self.request.user
        if user.has_perm("article.delete_comment"):
            return True
        obj = self.get_object()
        if obj.author == user:
            return True
        return False

    def get_success_url(self):
        from django.urls import reverse_lazy
        obj = self.get_object()
        forum_slug = obj.post.forum.slug
        post_slug = obj.post.slug
        return reverse_lazy('article:post_detail', kwargs={'forum':forum_slug, 'post':post_slug})