import hashlib
from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone

from author.models.role_model import Role


class UserManager(BaseUserManager):
    def create_user(self, email, username, first_name, last_name, password=None):
        if not email:
            raise ValueError("User must have an email")
        if not username:
            raise ValueError("User must have an username")
        email = email.lower()
        username = username.title()
        first_name = first_name.title()
        last_name = last_name.title()

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name

        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, first_name, last_name, password=None):
        user = self.create_user(
            email=email,
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    roles = models.ManyToManyField(Role, blank=True)
    email = models.EmailField(max_length=200, unique=True, verbose_name='email')
    username = models.CharField(max_length=200, unique=True, verbose_name='username')
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'username')

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    # def has_perm(self, perm, obj=None):
    #     return self.is_superuser
    #
    # def has_module_perms(self, app_label):
    #     return self.is_superuser

    class Meta:
        verbose_name_plural = 'Users'


class EmailVarification(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    email_confirmed = models.BooleanField(default=False)

    created_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='created_by')
    
    created_on = models.DateTimeField(default=timezone.now)

    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user} - {self.email_confirmed}"

class EmailConfirmed(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    activation_key = models.CharField(max_length=500)
    email_confirm = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name_plural = 'User Email Confirm'


@receiver(post_save, sender=User)
def create_user_email_confirmation(sender, instance, created, **kwargs):
    if created:
        dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        email_confirm_instance = EmailConfirmed(user=instance)
        user_encoded = f'{instance.email}-{dt}'.encode()
        activation_key = hashlib.sha224(user_encoded).hexdigest()
        email_confirm_instance.activation_key = activation_key
        email_confirm_instance.save()
