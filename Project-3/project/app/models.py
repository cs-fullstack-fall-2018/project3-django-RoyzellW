from django.contrib.auth.models import User
# from decimal import Decimal
# from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.
class Withdrawal(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)

class Deposit(models.Model):
    user = models.ForeignKey(User, default=None, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user)


class SignUp(models.Model):
    username = models.CharField(max_length=30, blank=False, default="Username")
    password = models.CharField(max_length=20, default="Password")
    balance = models.PositiveIntegerField()


    def __str__(self):
        return str(self.username)