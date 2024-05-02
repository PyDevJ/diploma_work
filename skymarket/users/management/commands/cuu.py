from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Create user."""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='user@sky.pro',
            first_name='User',
            last_name='SkyPro',
            phone=None,
            role='user',
            is_active=True
        )
        user.set_password('111')
        user.save()
