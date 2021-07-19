from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Address(models.Model):
    street_addr = models.CharField(max_length=200, null=True)


class Company(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(User, related_name='companies', null=True)
    addresses = models.ManyToManyField(Address, related_name='companies', null=True)
