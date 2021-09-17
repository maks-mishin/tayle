from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AccountForm, TransactionForm
from .models import Account, Transaction


@login_required
def my_accounts(request):
    accounts = Account.objects.filter(owner=request.user)
    form = AccountForm()
    return render(request, 'my_accounts.html', {'accounts': accounts, 'form': form})


def all_accounts(request):
    accounts = Account.objects.all()
    form = TransactionForm()
    return render(request, 'all_accounts.html', {'accounts': accounts, 'form': form})


@login_required
def account_detail(request, account_id: int):
    account = get_object_or_404(Account, id=account_id)
    return render(request, 'account_detail.html', {'account': account})


# создание нового кошелька
@login_required
def create_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            new_wallet = Account(
                owner=request.user,
                title=request.POST.get('title'),
                balance=float(request.POST.get('balance'))
            )
            new_wallet.save()
            return redirect('index')


@login_required
def delete_account(request, account_id: int):
    account = get_object_or_404(Account, id=account_id, owner=request.user)
    account.delete()
    return redirect('index')


@login_required
def transfer(request):
    form = TransactionForm(request.POST)

    if form.is_valid():
        sender = request.user
        receiver = request.POST.get('recipient')
        value = request.POST.get('value')

        new_transfer = Transaction(value=value, sender=sender, receiver=receiver)
        new_transfer.save()
        return redirect('index')


@login_required
def all_transfers(request):
    transfers = Transaction.objects.all()
    return render(request, 'transfers.html', {"transfers": transfers})
