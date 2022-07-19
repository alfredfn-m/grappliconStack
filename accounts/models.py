from tkinter import CASCADE
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

class Tournament(models.Model):
    host = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    name = models.CharField(max_length=100, default='Tournament Name')
    # When is the tournament
    date_of_tournament = models.DateTimeField()
    # Location of tournament
    address = models.CharField(max_length=100, default='Address')
    city = models.CharField(max_length=100, default='City')
    state_or_province = models.CharField(max_length=100, default='State or Province')
    nation = models.CharField(max_length=100, default='Nation')

    def __str__(self):
        return self.host.email + ', ' + self.name + ', ' + str(self.date_of_tournament.date())

class Champion(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    champion = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Bracket Information
    # SEX
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, default=MALE)
    # AGE
    age = models.CharField(max_length=5, choices=AGE_CHOICES, default=UPCOMING)
    # RANK
    rank = models.CharField(max_length=5, choices=RANK_CHOICES, default=WHITE)
    # weight
    weight = models.CharField(max_length=4, choices=WEIGHT_CHOICES, default=LESS125)
    # points
    points = models.IntegerField(default=0)
    
    def __str__(self):
        return self.champion.email

class Sex(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    # SEX
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, default=MALE)

    def __str__(self):
        return self.sex

class Age(models.Model):
    sex = models.ForeignKey(Sex, on_delete=models.CASCADE)
    # AGE
    age = models.CharField(max_length=5, choices=AGE_CHOICES, default=UPCOMING)

    def __str__(self):
        return self.age

class Rank(models.Model):
    Age = models.ForeignKey(Age, on_delete=models.CASCADE)
    # RANK
    rank = models.CharField(max_length=5, choices=RANK_CHOICES, default=WHITE)

    def __str__(self):
        return self.rank

class Weight(models.Model):
    Rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
    # weight
    weight = models.CharField(max_length=4, choices=WEIGHT_CHOICES, default=LESS125)
    number_of_competitors = models.IntegerField()

    def __str__(self):
        return self.weight

class Competitor(models.Model):
    weight = models.ForeignKey(Weight, on_delete=models.CASCADE)
    # Competitor Profile
    competitor = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    # Points Earned
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.competitor.email + ', ' + self.points