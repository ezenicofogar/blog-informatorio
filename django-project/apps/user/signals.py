from django.contrib.auth import get_user_model, models as auth_models
from django.contrib.contenttypes.models import ContentType
import logging; logger = logging.getLogger(__name__)

def create_Ejemplo_group(sender, **kwargs):
    # Ensure this runs only once per app load
    if kwargs.get('app_config', None) is None or kwargs['app_config'].label != 'user':
        return

    UserModel = get_user_model()
    UserModel_content_type = ContentType.objects.get_for_model(UserModel)

    Ejemplo_group, created = auth_models.Group.objects.get_or_create(name='Ejemplo')
    if created:
        logger.info('"Ejemplo" Group created.')

        view_user_perm   = auth_models.Permission.objects.get(codename='view_user', content_type=UserModel_content_type)
        Ejemplo_group.permissions.add(view_user_perm)
        logger.info('Added "view_user" Permission to "Ejemplo" Group.')

        change_user_perm = auth_models.Permission.objects.get(codename='change_user', content_type=UserModel_content_type)
        Ejemplo_group.permissions.add(change_user_perm)
        logger.info('Added "change_user" Permission to "Ejemplo" Group.')
