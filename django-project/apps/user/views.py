from django.views.generic import TemplateView

class TemporaryLoginView(TemplateView):
    template_name = 'login/login.html'
    extra_context = {
        'html_title': 'Inicio de sesión',
    }

class TemporaryRegisterView(TemplateView):
    template_name = 'login/register.html'
    extra_context = {
        'html_title': 'Registro',
    }

class TemporaryResetView(TemplateView):
    template_name = 'login/reset.html'
    extra_context = {
        'html_title': 'Restablecimiento',
    }

class TemporaryValidatorView(TemplateView):
    template_name = 'login/validator.html'
    extra_context = {
        'html_title': 'Validación',
    }
