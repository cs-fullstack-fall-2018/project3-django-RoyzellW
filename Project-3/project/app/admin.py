from django.contrib import admin
from .models import Withdrawal, Deposit, SignUp
# Register your models here.
admin.site.register(Withdrawal)
admin.site.register(Deposit)
admin.site.register(SignUp)

