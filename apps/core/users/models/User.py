import uuid

from django.contrib.auth.models import Group, Permission, AbstractUser
from django.db import models
from django.utils.translation import gettext as _

from apps.core.users.models.UserManager import UserManager


class User(AbstractUser):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    first_name = models.CharField(max_length=60)
    middle_name = models.CharField(max_length=60, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=60)
    username = models.CharField(verbose_name="CPF", max_length=60, unique=True, default=None, blank=True)
    email = models.EmailField(max_length=255, unique=True)
    dob = models.DateField(default=None, blank=True, null=True)

    is_email_verified = models.BooleanField(default=False, blank=True)
    is_active = models.BooleanField(default=True, blank=True)

    # Need to copy this, otherwise the django police will come after me
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_groups",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="user_permissions",
        related_query_name="user",
    )

    USERNAME_FIELD = 'username'

    objects = UserManager()

    """
    A list of fields required when creating an user via `createsuperuser`
    USERNAME_FIELD and password are already required
    """
    REQUIRED_FIELDS = ['first_name', 'last_name', 'email']

    class Meta:
        verbose_name = _("Account")
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
            full_name = '%s %s' % (self.first_name, self.last_name)
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

    @property
    def superuser(self):
        return self.is_superuser

    def __str__(self):
        return self.full_name

def auto_generate_username(sender, instance, **kwargs):
    if not instance.username:
        instance.username = instance.first_name + "_" + uuid.uuid4().hex[:6]


models.signals.pre_save.connect(auto_generate_username, sender=User)

def generate_middle_name(sender, instance, **kwargs):
    name_array = instance.last_name.split()
    if len(name_array) > 1:
        instance.last_name = name_array.pop()
        instance.middle_name = ' '.join(name_array)

models.signals.pre_save.connect(generate_middle_name, sender=User)
