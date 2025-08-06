from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from apps.post.models import Post

# Create your views here.
class IndexView(TemplateView):
    template_name = 'html5.html'


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    context_object_name = "posts_list"

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


