from django.core.management.base import BaseCommand
from accounts.models import User

class Command(BaseCommand):
    help = 'Creating a superuser'

    def handle(self, *args, **options):
        if not User.objects.filter(email="admin@gmail.com").exists():
            User.objects.create_superuser("admin@admin.com", "admin")
        else:
            u = User.objects.get(email="admin@gmail.com")
            u.delete()
            User.objects.create_superuser("admin@admin.com", "admin")
