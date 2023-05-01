from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from backend.core.models import MetaModel
from rest_framework_simplejwt.tokens import RefreshToken


class UserManager(BaseUserManager):
    """Custom user manager"""

    def create_user(self, email, username, password=None, **extra_fields):
        """Creates and saves a new user"""
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')
        user = self.model(username=username, email=self.normalize_email(email), **extra_fields)
        user.set_password(password) 
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        """Creates and saves a new superuser"""
        if password is None:
            raise TypeError('Superusers must have a password')
        user = self.create_user(email, username, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db) 

        return user


class User(AbstractBaseUser, MetaModel):
    """Custom user model that supports using email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser
    
    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }  