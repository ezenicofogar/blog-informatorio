from django.contrib.auth.forms import UserCreationForm

# Se agregan los campos first_name y last_name al formulario de registro
class FullUserCreationForm(UserCreationForm):
    class Meta:
        model = UserCreationForm.Meta.model
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name',)