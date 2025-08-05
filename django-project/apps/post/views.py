from django.views.generic import TemplateView

#from post.models import Post

# Create your views here.
class IndexView(TemplateView):
    template_name = 'html5.html'

class PostDetailView(TemplateView):
    #model = Post
    template_name = 'post/post_detail.html' # no está definido ese archivo?

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        #post_slug = self.kwargs.get('slug')
        #post = Post.objects.get(slug=post_slug) #no está definido esa función? 
        #context['post'] = post
        #return context


