from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Profile

class EmployeeInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(BaseUserAdmin):
    inlines = [EmployeeInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'profile__bio', 'profile__picture')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
