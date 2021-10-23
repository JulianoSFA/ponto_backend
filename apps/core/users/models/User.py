from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models

from apps.core.models.UserManager import UserManager


class User(AbstractUser, PermissionsMixin):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=60)
    username = models.CharField("CPF", max_length=60, unique=True, default=None, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    dob = models.DateField(default=None, blank=True, null=True)

    is_email_verified = models.BooleanField(default=False, blank=True)
    is_active = models.BooleanField(default=True, blank=True)

    USERNAME_FIELD = 'username'

    objects = UserManager()

    """
    A list of fields required when creating an user via `createsuperuser`
    USERNAME_FIELD and password are already required
    """
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        verbose_name = "Account"
        ordering = ['-id']
        db_table = 'users'


    @property
    def full_name(self):
        """
        Get the user full name.
        :return: string
        """
        if self.middle_name:
            full_name = '%s %s %s' % (self.first_name, self.middle_name, self.last_name)
        else:
            full_name = self.get_full_name()
        return full_name.strip()

    @property
    def short_name(self):
        """
        Get the user first and last name.
        :return: string
        """
        short_name = '%s %s' % (self.first_name, self.last_name)
        return short_name

    @property
    def name(self):
        """
        Get the user name.
        :return: string
        """
        return self.first_name

    def __str__(self):
        return self.full_name

def generate_middle_name(sender, instance, **kwargs):
    name_array = instance.last_name.split()
    if len(name_array) > 1:
        instance.last_name = name_array.pop()
        instance.middle_name = ' '.join(name_array)


models.signals.pre_save.connect(generate_middle_name, sender=User)