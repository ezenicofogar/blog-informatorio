from django.shortcuts import render

from django.views import generic, View
from django.contrib.auth import mixins, get_user_model, views as auth_views
from django.urls import reverse_lazy
from . import forms
from .models import Profile as ProfileModel

UserModel = get_user_model()


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

class SelfDetailView(mixins.LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        from django.shortcuts import redirect
        return redirect('user:user_detail', request.user.pk)

class SelfUpdateView(mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'user/userUpdate.html'
    model = UserModel
    fields = ['first_name', 'last_name', 'email']
    def get_object(self, queryset=None):
        return self.request.user
    def get_success_url(self):
        return reverse_lazy('user:self_detail')
    extra_context = {
        'html_title': 'Editar mi perfil',
    }

class SelfUpdateProfileView(mixins.LoginRequiredMixin, generic.UpdateView):
    template_name = 'user/userUpdateProfile.html'
    model = ProfileModel
    fields = ['bio', 'picture']
    def get_object(self, queryset=None):
        return self.request.user.profile
    def get_success_url(self):
        return reverse_lazy('user:self_detail')
    extra_context = {
        'html_title': 'Editar mi biografía'
    }


# Perfil del usuario (general)

class UserDetailView(mixins.LoginRequiredMixin, generic.DetailView):
    template_name = 'user/userDetail.html'
    queryset = UserModel.objects.all()
    extra_context = {
        'html_title': 'Perfil de usuario'
    }

class UserUpdateView(mixins.PermissionRequiredMixin, generic.UpdateView):
    template_name = 'user/userUpdate.html'
    permission_required = ['auth.change_user',]
    model = UserModel
    fields = ['first_name', 'last_name', 'email', 'is_active']
    def get_success_url(self):
        pk = self.get_object().pk
        return reverse_lazy('user:user_detail', kwargs={'pk': pk})
    extra_context = {
        'html_title': 'Editar perfil de usuario'
    }

class UserUpdateProfileView(mixins.PermissionRequiredMixin, generic.UpdateView):
    template_name = 'user/userUpdateProfile.html'
    permission_required = ['auth.change_user',]
    model = ProfileModel
    fields = ['bio', 'picture']
    def get_success_url(self):
        pk = self.get_object().pk
        return reverse_lazy('user:user_detail', kwargs={'pk': pk})
    extra_context = {
        'html_title': 'Editar perfil de usuario'
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
            { 'text': 'Ir a mi perfil', 'url': 'user:self_detail' },
        ],
    }

class PasswordChangeDoneView(auth_views.PasswordChangeDoneView):
    template_name = 'user/authDone.html'
    extra_context = {
        'html_title': 'Contraseña cambiada',
        'done_text': 'Tu contraseña ha sido cambiada con éxito.',
        'links': [
            { 'text': 'Ir a mi perfil', 'url': 'user:self_detail' },
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
