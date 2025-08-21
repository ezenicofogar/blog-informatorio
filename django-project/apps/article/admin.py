from django.contrib import admin
from . import models

# Register your models here.
class ForumAdmin(admin.ModelAdmin):
    model = models.Forum
    list_display = ['__str__', 'title', 'author', 'created_at']
    fieldsets = [
        (None, {'fields': ['title', 'short', 'cover']},),
        ('Adicionales', {'fields': ['slug', 'author']},),
    ]

class PostAdmin(admin.ModelAdmin):
    model = models.Post
    list_display = ['__str__', 'title', 'author', 'created_at']
    fieldsets = [
        (None, {'fields': ['title', 'preimagebody', 'image', 'body']},),
        ('Adicionales', {'fields': ['slug', 'author']},),
        ('Relaciones', {'fields': ['forum']},),
    ]

class HighlightedAdmin(admin.ModelAdmin):
    model = models.Highlighted
    list_display = ['post']

class CommentAdmin(admin.ModelAdmin):
    model = models.Comment
    list_display = ['author', 'post', 'created_at', 'last_update']
    fields = ['body', 'author', 'post']

admin.site.register(models.Forum, ForumAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Highlighted, HighlightedAdmin)
admin.site.register(models.Comment, CommentAdmin)
