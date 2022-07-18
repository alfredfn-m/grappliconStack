from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .theChoices import *
from django.contrib.auth.base_user import BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)




class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'),max_length=50, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # additional information
    # SEX
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, default=MALE)
    # AGE
    age = models.CharField(max_length=5, choices=AGE_CHOICES, default=UPCOMING)
    # RANK
    rank = models.CharField(max_length=5, choices=RANK_CHOICES, default=WHITE)
    # weight
    weight = models.CharField(max_length=4, choices=WEIGHT_CHOICES, default=LESS125)
    # isHost
    is_Host = models.BooleanField(default=False)
    # isCompetitor
    is_Competitor = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email