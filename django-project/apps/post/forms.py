from django import forms
from apps.post.models import Comment


class PostFilterForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        widget=forms.TextInput(
            attrs={'placeholder': 'Buscar...',
                   'class': 'w-full p-2 bg-red-200'}
        )
    )
    order_by = forms.ChoiceField(
        choices=[
            ('date', 'Fecha'),
            ('title', 'Título'),
            ('-created_at', 'Más recientes'),
            ('created_at', 'Más antiguos'),
            ('-comments_count', 'Más comentados')
        ],
        required=False,
        widget=forms.Select(
            attrs={'class': 'w-full p-2 bg-red-400'}
        )
    )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['content']

        labels = {
            'content':  'Comentario'
        }

        widget = {
            'content': forms.Textarea(
                attrs={
                    'rows': 3, 'placeholder': 'Escribe tu comentario...', 'class': 'p-2'
                }
            )
        }
        help_texts = {
            'content': 'Escribe tu comentario aquí.'
        }
        error_messages = {
            'content': {
                'required': 'El campo comentario no puede estar vacío.',
                'max_length': 'El comentario es demasiado largo.'
            }
        }
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['content'].widget.attrs.update({'class': 'p-2'})
            self.fields['content'].help_text = 'Escribe tu comentario aquí.'
            self.fields['content'].error_messages = {
                'required': 'El campo comentario no puede estar vacío.',
                'max_length': 'El comentario es demasiado largo.'
            }
            self.fields['content'].label = 'Comentario'
            self.fields['content'].widget.attrs.update({'rows': 3, 'placeholder': 'Escribe tu comentario...'})
          