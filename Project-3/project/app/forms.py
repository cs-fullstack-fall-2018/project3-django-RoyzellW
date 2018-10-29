from django import forms
from .models import SignUp, Deposit, Withdrawal

class SignUpForm(forms.ModelForm):
    username = forms.CharField(label="id_username")
    password = forms.CharField(label="id_password")

    class Meta:
        model = SignUp
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ['amount']


class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = Withdrawal
        fields = ['amount']
