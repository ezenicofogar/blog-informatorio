from django.db import models
import uuid
import os
from django.conf import settings
from django.utils import timezone
from django.utils.text import slugify
#from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, MaxLengthValidator

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, validators=[MinLengthValidator(3), MaxLengthValidator(50)])
    slug = models.SlugField(unique=True, max_length=100, blank=True, null=True)
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('category_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
#TODO: NO ESTÁ DEFINIDO AUTH_USER_MODEL, DEBE SER CONFIGURADO EN settings.py??
class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=100, validators=[MinLengthValidator(5), MaxLengthValidator(100)])
    slug = models.SlugField(unique=True, max_length=200, blank=True, null=True)
    content = models.TextField(max_length=10000, validators=[MinLengthValidator(10)])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name='posts')
    allow_comments = models.BooleanField(default=True)
    #image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True, help_text="Comma-separated list of tags")
    is_published = models.BooleanField(default=True)
    #class Meta:
        #ordering = ['-created_at']
        #verbose_name = 'Post'
        #verbose_name_plural = 'Posts'
    
    #def get_absolute_url(self):
        #from django.urls import reverse
        #return reverse('post_detail', kwargs={'slug': self.slug})
    #def save(self, *args, **kwargs):
        #if not self.slug:
            #self.slug = slugify(self.title)
        #super().save(*args, **kwargs)
        #ó
    def generate_unique_slug(self):
        base_slug = slugify(self.title)
        unique_slug = base_slug
        count = 1
        while Post.objects.filter(slug=unique_slug).exists():
            unique_slug = f"{base_slug}-{count}"
            count += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self.generate_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    

    @property
    def amount_of_comments(self):
        return self.comments.count()
    @property
    def amount_of_likes(self):
        return self.likes.count()
    @property
    def amount_of_images(self):
        return self.images.count()
    #@property
    #def amount_of_tags(self):
        #return len(self.tags.split(',')) if self.tags else 0

class Comment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField(max_length=300, validators=[MinLengthValidator(1), MaxLengthValidator(300)])
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    #class Meta:
        #ordering = ['created_at']
        #verbose_name = 'Comment'
        #verbose_name_plural = 'Comments'

    def __str__(self):
        return f'Comentario de: {self.author} en {self.post} : {self.content[:50]}...'

def get_image_path(instance, filename):
    # Generate a unique filename using UUID
    #ext = filename.split('.')[-1]
    #unique_filename = f"{uuid.uuid4()}.{ext}"
    #return os.path.join('post_images', unique_filename)
    #ó
    post_id = instance.post.id
    images_count = instance.post.images.count()
    file_extension = os.path.splitext(filename)
    new_filename = f"{post_id}_{images_count + 1}{file_extension}"
    #TODO: ESTABLECER RUTA O CARPETA PARA LA IMAGEN por ejemplo: 'post/cover/
    return os.path.join('post_images', new_filename)

class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=get_image_path)
    caption = models.CharField(max_length=200, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)


    #class Meta:
        #verbose_name = 'Post Image'
        #verbose_name_plural = 'Post Images'

    def __str__(self):
        return f'Imagen de {self.post.title} - {self.caption[:20] if self.caption else "Sin título"}'



