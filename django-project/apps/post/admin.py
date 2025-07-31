from django.contrib import admin
from .models import Category, Post, PostImage,  Category, Comment


class CategoryAdmin(admin.ModelAdmin):
    #list_display = ('name', 'slug')
    #prepopulated_fields = {'slug': ('name',)}
    list_display = ('title',)
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'author', 'allow_comments', 'created_at', 'updated_at', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'author', 'created_at', 'allow_comments')
    search_fields = ('id', 'title', 'content', 'author__username')
    ordering = ('-created_at', )

class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'caption', 'active', 'created_at')
    list_filter = ('active', 'created_at')
    search_fields = ('post__id', 'post__title', 'image')
    #search_fields = ('caption',)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'author', 'created_at')
    list_filter = ('created_at', 'author')
    search_fields = ('id', 'author__username', 'post__title')
    ordering = ('-created_at', )

def activate_images(modeladmin, request, queryset):
    update = queryset.update(active=True)
    modeladmin.message_user(request, f"{update} imágenes activadas correctamente.")

activate_images.short_description = "Activar imágenes seleccionadas"

def deactivate_images(modeladmin, request, queryset):
    update = queryset.update(active=False)
    modeladmin.message_user(request, f"{update} imágenes desactivadas correctamente.")

deactivate_images.short_description = "Desactivar imágenes seleccionadas"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostImage, PostImageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.add_action(activate_images, 'activate_images')
admin.site.add_action(deactivate_images, 'deactivate_images')