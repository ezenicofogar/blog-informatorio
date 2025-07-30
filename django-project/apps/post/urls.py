from django.urls import path
from apps.post import views as view

app_name = 'post'

urlpatterns = [path('post/<slug:slug>/', view.PostDetailView.as_view(), name='post_detail')]

#no está definido la función PostDetailView.as_view() en views.py, por lo que se debe crear.


