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
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('post_detail', kwargs={'slug': self.slug})
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    



