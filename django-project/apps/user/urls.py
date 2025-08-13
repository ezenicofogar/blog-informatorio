"""
Configuración de URL para la aplicación user.

La lista `urlpatterns` enruta las URLs a las vistas. Para más información, consulta:
    https://docs.djangoproject.com/es/5.2/topics/http/urls/
"""
from django.urls import path
from . import views_temp, views

app_name = "user"

urlpatterns = [
    # Registro de usuario
    path('register/', views.CreationView.as_view(), name='register'),

    # Self
    path('', views.SelfDetailView.as_view(), name='self_detail'),
    path('edit/', views.SelfUpdateView.as_view(), name='self_update'),
    path('edit/bio/', views.SelfUpdateProfileView.as_view(), name='self_update_profile'),

    # User
    path('<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('<int:pk>/edit/', views.UserUpdateView.as_view(), name='user_update'),
    path('<int:pk>/edit/bio/', views.UserUpdateProfileView.as_view(), name='user_update_profile'),

    # Auth views de Django
    # 
    # https://docs.djangoproject.com/en/5.2/topics/auth/default/#module-django.contrib.auth.views
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/complete/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),

    # Templates con estilos pero sin funcionalidad
    # TODO: Implementar estos estilos en los otros templates
    path("test/login/", views_temp.TemporaryLoginView.as_view()),
    path("test/register/", views_temp.TemporaryRegisterView.as_view()),
    path("test/reset/", views_temp.TemporaryResetView.as_view()),
    path("test/validator/", views_temp.TemporaryValidatorView.as_view()),
]
