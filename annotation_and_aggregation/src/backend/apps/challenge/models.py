from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Company(models.Model):
    name = models.CharField(max_length=200)
    owner = models.ForeignKey(User, related_name='companies', null=True, on_delete=models.CASCADE)
    assets_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    liabilities_value = models.DecimalField(max_digits=10, decimal_places=2, default=0)
