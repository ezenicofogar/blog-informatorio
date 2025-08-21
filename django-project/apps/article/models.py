from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()

class Forum(models.Model):
    class Meta:
        verbose_name = 'foro'
        verbose_name_plural = 'foros'

    slug = models.SlugField(verbose_name='slug', unique=True, max_length=24)

    title = models.CharField(verbose_name='título', max_length=128)
    short = models.CharField(verbose_name='resumen', max_length=256)
    cover = models.ImageField(verbose_name='portada', upload_to='forum_cover_images')

    author = models.ForeignKey(verbose_name='autor', to=UserModel, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='creación', auto_now_add=True)

    def __str__(self) -> str:
        return self.slug

class Post(models.Model):
    class Meta:
        verbose_name = 'publicación'
        verbose_name_plural = 'publicaciones'
        constraints = [
            models.UniqueConstraint(fields=['forum', 'slug'], name='unique_post_forum_slug')
        ]
        indexes = [
            models.Index(fields=['forum', 'slug'], name='idx_post_forum_slug')
        ]

    forum = models.ForeignKey(verbose_name='tema', to=Forum, on_delete=models.CASCADE)
    slug = models.SlugField(verbose_name='slug', max_length=48)

    title = models.CharField(verbose_name='título', max_length=128)
    preimagebody = models.TextField(verbose_name='texto previo', blank=True, default=None)
    image = models.ImageField(verbose_name='imágen', upload_to='post_images')
    body = models.TextField(verbose_name='texto principal')

    author = models.ForeignKey(verbose_name='autor', to=UserModel, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(verbose_name='creación', auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.forum.slug}/{self.slug}'

class Highlighted(models.Model):
    class Meta:
        verbose_name = 'destacado'
        verbose_name_plural = 'destacados'
    post = models.ForeignKey(verbose_name='publicación destacada', to=Post, on_delete=models.CASCADE)

class Comment(models.Model):
    class Meta:
        verbose_name = 'comentario'
        verbose_name_plural = 'comentarios'
    author = models.ForeignKey(verbose_name='autor', to=UserModel, on_delete=models.CASCADE)
    post = models.ForeignKey(verbose_name='publicación', to=Post, on_delete=models.CASCADE)
    body = models.TextField(verbose_name='texto del comentario')
    created_at = models.DateTimeField(verbose_name='creación', auto_now_add=True)
    last_update = models.DateTimeField(verbose_name='última modificación', auto_now=True)
