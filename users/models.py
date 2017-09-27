from django.contrib.auth.models import AbstractUser
from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=120)


class User(AbstractUser):
    class ROLES:
        CUSTOMER = 0
        EMPLOYEE = 1
        _CHOICES = ((CUSTOMER, 'Customer'), (EMPLOYEE, 'Employee'))

    department = models.ForeignKey(Department, related_name='consultants',
                                   on_delete=models.CASCADE)
    role = models.PositiveSmallIntegerField(choices=ROLES._CHOICES,
                                            default=ROLES.CUSTOMER)
