from django.db import models, transaction
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.core.management import call_command
from django.conf import settings

from .managers import CustomUserManager

# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    profile_image = models.ImageField(
        upload_to='profile_image',
        blank=True
    )

    @transaction.atomic
    def save(self, *args, **kwargs):
        # `save` method of your `User` model

        # if user hasnt ID - is creationg operation
        created = self.id is None
        super(User, self).save(*args, **kwargs)

        # after save user has ID
        # add user to group only after creating
        if created:
            user = self

            if not Group.objects.all():
                call_command('creategroups')

            group = None
            if not user.is_admin:
                group = Group.objects.get(name=settings.GROUP_BASE)

            if group:
                group.user_set.add(self)

    def __str__(self):
        return self.email
