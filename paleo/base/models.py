from django.db import models

from django.config import settings


class Service(models.Model):
    slug = models.SlugField(max_length=16, primary_key=True)


class User(models.Model):
    auth_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        primary_key=True,
        related_name='paleo_user'
    )

    allowed_services = models.ManyToManyField(Service, related_name='users')


class Team(models.Model):
    members = models.ManyToManyField(User, related_name='teams')


class Group(models.Model):
    teams = models.ManyToManyField(Team, related_name='groups')

    allowed_services = models.ManyToManyField(Service, related_name='groups')
