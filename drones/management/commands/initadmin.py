__author__ = 'dkarchmer@gmail.com'

from django.conf import settings
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):

    def handle(self, *args, **options):
        User = get_user_model()

        if User.objects.count() == 0:
            print('Creating super user...')
            admin = User.objects.create_superuser(
                email=settings.ADMIN_EMAIL,
                username=settings.ADMIN_USERNAME,
                password=settings.ADMIN_INITIAL_PASSWORD)
            admin.is_active = True
            admin.is_superuser = True
            admin.is_staff = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
