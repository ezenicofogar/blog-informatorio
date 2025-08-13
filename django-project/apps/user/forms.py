from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile as ProfileModel

UserModel = get_user_model()

# Se agregan los campos first_name y last_name al formulario de registro
class FullUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm.Meta.model
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')
