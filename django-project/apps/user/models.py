from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save

AuthUserModel = get_user_model()

class Profile(models.Model):
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
    user = models.OneToOneField(to=AuthUserModel, on_delete=models.CASCADE, primary_key=True)
    bio = models.TextField(verbose_name="Biografía", blank=True, default='', max_length=511)
    picture = models.ImageField(verbose_name="Foto de perfil", upload_to='profile_pictures/', blank=True, default=None)

# Crear perfil al crear usuario
def link_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
post_save.connect(link_profile, sender=AuthUserModel, weak=False)
