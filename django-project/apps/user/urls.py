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

    # Perfil del usuario
    path('', views.ProfileSelfView.as_view(), name='profile_self'),

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
