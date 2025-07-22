"""
Configuración de URL para la aplicación user.

La lista `urlpatterns` enruta las URLs a las vistas. Para más información, consulta:
    https://docs.djangoproject.com/es/5.2/topics/http/urls/
"""
from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.TemporaryLoginView.as_view(), name="login"),
    path("register/", views.TemporaryRegisterView.as_view(), name="register"),
    path("reset/", views.TemporaryResetView.as_view(), name="reset"),
    path("validator/", views.TemporaryValidatorView.as_view(), name="validator"),
]
