from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import DepositForm, WithdrawalForm
from .models import Withdrawal, Deposit
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



# create a user
def createUser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created succesfully')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'app/index.html', {'form': form})


# log in to your account
def logIn(request):
    if request.user.is_authenticated:
        return redirect('user_page')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('user_page')
        else:
            messages.error(request, 'Error wrong username/password')

    return render(request, 'app/login.html')


# log out of your account
def logout(request):
    auth.logout(request)
    return redirect('logout')


# direct to admin page
def user_page(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return render(request, 'app/user_page.html')


@login_required()
def diposit_view(request):
    if not request.user.is_authenticated:
        raise get_object_or_404
    else:
        title = "Deposit"
        form = DepositForm(request.POST or None)

        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.user = request.user
            # adds users deposit to balance.
            deposit.user.balance += deposit.amount
            deposit.user.save()
            deposit.save()
            messages.success(request, 'You Have Deposited {} $.'
                             .format(deposit.amount))
            return redirect("user_page")

        context = {
            "title": title,
            "form": form
        }
        return render(request, "app/user_page.html", context)


@login_required()
def withdrawal_view(request):
    if not request.user.is_authenticated:
        raise get_object_or_404
    else:
        title = "Withdraw"
        form = WithdrawalForm(request.POST or None)

        if form.is_valid():
            withdrawal = form.save(commit=False)
            withdrawal.user = request.user

            # checks if user is tring Withdraw more than his balance.
            if withdrawal.user.balance >= withdrawal.amount:
                # substracts the users withdrawal from balance
                withdrawal.user.balance -= withdrawal.amount
                withdrawal.user.save()
                withdrawal.save()
                messages.error(request, 'You Have Withdrawn {} $.'
                               .format(withdrawal.amount))
                return redirect("user_page")

            else:
                messages.error(
                    request,
                    'You Can Not Withdraw More Than Your Balance.'
                )

        context = {
            "title": title,
            "form": form
        }
        return render(request, "app/user_page.html", context)

