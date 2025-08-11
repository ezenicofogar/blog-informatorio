from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.post.models import Post, PostImage, Comment
from django.db.models import Count
from apps.post.forms import PostFilterForm, PostCreateForm, CommentForm
from django.urls import reverse, reverse_lazy
from django.shortcuts import get_object_or_404
from django.conf import settings

# Create your views here.
class IndexView(TemplateView):
    template_name = 'html5.html'


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = "posts_list"

    paginate_by = 1

    def get_queryset(self):
        queryset = Post.objects.all().annotate(comments_count=Count('comments'))
        search_query = self.request.GET.get('search_query', '')
        order_by = self.request.GET.get('order_by', '-created_at')

        if search_query:
            queryset = queryset.filter(title__icontains=search_query) | queryset.filter(
                author__username__icontains=search_query)

        return queryset.order_by(order_by)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter_form'] = PostFilterForm(self.request.GET)

        if context.get('is_paginated', False):
            query_params = self.request.GET.copy()
            query_params.pop('page', None)

            pagination = {}
            page_obj = context['page_obj']
            paginator = context['paginator']

            if page_obj.number > 1:
                pagination['first_page'] = f'?{query_params.urlencode()}&page={paginator.page_range[0]}'

            if page_obj.has_previous():
                pagination['previous_page'] = f'?{query_params.urlencode()}&page={page_obj.number - 1}'

            if page_obj.has_next():
                pagination['next_page'] = f'?{query_params.urlencode()}&page={page_obj.number + 1}'

            if page_obj.number < paginator.num_pages:
                pagination['last_page'] = f'?{query_params.urlencode()}&page={paginator.num_pages}'

            context['pagination'] = pagination

        return context


class PostDetailView(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        active_images = self.object.images.filter(active=True)

        context['active_images'] = active_images
        context['add_comment_form'] = CommentForm()

        edit_comment_id = self.request.GET.get('edit_comment')
        if edit_comment_id:
            comment = get_object_or_404(Comment, id=edit_comment_id)

            if comment.author == self.request.user:
                context['edit_comment_id'] = comment.id
                context['edit_comment_form'] = CommentForm(instance=comment)
            else:
                context['edit_comment_id'] = None
                context['edit_comment_form'] = None

        delete_comment_id = self.request.GET.get('delete_comment')
        if delete_comment_id:
            comment = get_object_or_404(Comment, id=delete_comment_id)

            if (comment.author == self.request.user or
                    (comment.post.author == self.request.user and not
                     comment.author.is_admin and not
                     comment.author.is_superuser) or
                    self.request.user.is_superuser or
                    self.request.user.is_staff or
                    self.request.user.is_admin
                ):
                context['deleting_comment_id'] = comment.id
            else:
                context['deleting_comment_id'] = None        

        return context

class PostCreateView(CreateView):
    model = Post
    form_class = PostCreateForm
    template_name = 'post/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  
        post = form.save()

        images = self.request.FILES.getlist('images')

        if images:
            for image in images:
                PostImage.objects.create(post=post, image=image)
        else:
            PostImage.objects.create(
                post=post, image=settings.DEFAULT_POST_IMAGE)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('post:post_detail', kwargs={'slug': self.object.slug})


class PostUpdateView(UpdateView):
    model = Post
    template_name = 'post/post_update.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('post:post_detail', kwargs={'slug': self.object.slug})   

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/post_confirm_delete.html'
    success_url = reverse_lazy('post:post_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post_slug = self.kwargs.get('slug')
        post = Post.objects.get(slug=post_slug)
        context['post'] = post
        return context

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'post/post_detail.html',

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = Post.objects.get(slug=self.kwargs['slug'])

        return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('post:post_detail', kwargs={'slug': self.object.post.slug})
    

class CommentUpdateView(UpdateView):
    model = Comment
    fields = ['text']
    template_name = 'comments/comment_update.html'
    def get_success_url(self):
        return reverse_lazy('post:post_detail', kwargs={'slug': self.object.post.slug})
    
class CommentDeleteView(DeleteView):
    model = Comment
    template_name = 'comments/comment_delete.html'
    success_url = reverse_lazy('comment_list')
    def get_queryset(self):
        # Sobrescribir este método para restringir qué comentarios un usuario puede eliminar.
        return Comment.objects.filter(author=self.request.user)
