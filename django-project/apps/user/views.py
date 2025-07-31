from django.views import generic
from django.contrib.auth import mixins
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import forms


# Registro de usuario

class CreationView(generic.CreateView):
    form_class = forms.FullUserCreationForm
    template_name = 'user/authForm.html'
    success_url = reverse_lazy('user:login')
    extra_context = {
        'html_title': 'Registrarse',
        'form_action': 'Registrarse',
        'links': [
            { 'text': 'Ya tengo una cuenta', 'url': 'user:login' },
            { 'text': 'Olvidé mi contraseña', 'url': 'user:password_reset' },
        ],
    }


# Perfil del usuario (mi perfil)

class ProfileSelfView(mixins.LoginRequiredMixin, generic.TemplateView):
    template_name = 'user/profileSelf.html'
    extra_context = {
        'html_title': 'Mi perfil',
        'links': [
            { 'text': 'Cambiar mi contraseña', 'url': 'user:password_change' },
        ],
    }


# Auth views de Django
# 
# https://docs.djangoproject.com/en/5.2/topics/auth/default/#module-django.contrib.auth.views

class LoginView(auth_views.LoginView):
    template_name = 'user/authForm.html'
    extra_context = {
        'html_title': 'Iniciar sesión',
        'form_action': 'Entrar',
        'links': [
            { 'text': 'No tengo una cuenta', 'url': 'user:register' },
            { 'text': 'Olvidé mi contraseña', 'url': 'user:password_reset' },
        ],
    }

class LogoutView(auth_views.LogoutView):
    ...

class PasswordChangeView(auth_views.PasswordChangeView):
    template_name = 'user/authForm.html'
    extra_context = {
        'html_title': 'Cambiar contraseña',
        'form_action': 'Cambiar',
        'links': [
            { 'text': 'Ir a mi perfil', 'url': 'user:profile_self' },
        ],
    }

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'user/authDone.html'
    extra_context = {
        'html_title': 'Contraseña cambiada',
        'done_text': 'Tu contraseña ha sido cambiada con éxito.',
        'links': [
            { 'text': 'Ir a mi perfil', 'url': 'user:profile_self' },
        ],
    }

class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'user/authForm.html'
    extra_context = {
        'html_title': 'Recuperar contraseña',
        'form_action': 'Recuperar',
        'links': [
            { 'text': 'No tengo una cuenta', 'url': 'user:register' },
            { 'text': 'Iniciar sesión', 'url': 'user:login' },
        ],
    }

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'user/authDone.html'
    extra_context = {
        'html_title': 'Código enviado',
        'done_text': 'Se ha enviado un código para recuperar tu contraseña. Por favor, verifica tu correo electrónico.'
        # 'links': [
        #     { 'text': 'Ir al inicio', 'url': '???' },
        # ],
    }

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'user/authForm.html'
    extra_context = {
        'html_title': 'Confirmar recuperación',
        'form_action': 'Confirmar',
        # 'links': [
        #     { 'text': 'Ir al inicio', 'url': '???' },
        # ],
    }

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'user/authDone.html'
    extra_context = {
        'html_title': 'Contraseña cambiada',
        'done_text': 'Tu contraseña ha sido cambiada con éxito.'
        # 'links': [
        #     { 'text': 'Ir al inicio', 'url': '???' },
        # ],
    }
