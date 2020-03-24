from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

from django.contrib.contenttypes.models import ContentType
from django.conf import settings

from whatDo.models import Activity, Effort

class Command(BaseCommand):
    help = 'Creating group'

    def handle(self, *args, **options):
        # Owner group
        group, created = Group.objects.get_or_create(name=settings.GROUP_BASE)
        if group:
            # models with all permissions
            allowed_models = [Effort]
            for allowed_model in allowed_models:
                content_type = ContentType.objects.get_for_model(allowed_model)
                permissions = Permission.objects.filter(content_type=content_type)
                for permission in permissions:
                    group.permissions.add(permission)
            # models with specific permissions
            allowed_models = [Activity]
            for allowed_model in allowed_models:
                content_type = ContentType.objects.get_for_model(allowed_model)
                permissions = Permission.objects.filter(content_type=content_type)
                for permission in permissions:
                    if 'add' in permission.codename or 'view' in permission.codename:
                        group.permissions.add(permission)
            print('Base group created')
