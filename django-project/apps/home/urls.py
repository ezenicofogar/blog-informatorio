from django.urls import path
from django.views.generic import TemplateView
from apps.article.models import Highlighted, Forum

app_name = 'home'

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='index.html',
        extra_context={
            'highlighted': Highlighted.objects.all(),
            'forums': Forum.objects.filter(author=None).order_by('-created_at')[:4],
        },
        ), name='index'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
]
