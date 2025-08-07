from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.post.models import Post
from django.db.models import Count
from apps.post.forms import PostFilterForm


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
    #model = Post
    template_name = 'post/post_detail.html'

class PostCreateView(CreateView):
    #model = Post
    template_name = 'post/post_form.html'

class PostUpdateView(UpdateView):
    #model = Post
    template_name = 'post/post_update.html'

class PostDeleteView(DeleteView):
    #model = Post
    template_name = 'post/post_confirm_delete.html'

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #post_slug = self.kwargs.get('slug')
        #post = Post.objects.get(slug=post_slug) #no está definido esa función? 
        #context['post'] = post
        #return context


