from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from users.models import User
from .forms import AccountForm
from .models import Account, Transaction


# отображает список счетов пользователя
# баланс - дата создания - кнопка удаления
def my_accounts(request):
    accounts = Account.objects.filter(owner=request.user)
    form = AccountForm()
    return render(request, 'my_accounts.html', {'accounts': accounts, 'form': form})


def all_accounts(request):
    accounts = Account.objects.all()
    return render(request, 'all_accounts.html', {'accounts': accounts})


def account_detail(request, account_id: int):
    account = get_object_or_404(Account, id=account_id)
    return render(request, 'account_detail.html', {'account': account})


# создание нового кошелька
def create_wallet(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            new_wallet = Account(owner=request.user, balance=float(request.POST.get('balance')))
            new_wallet.save()
            return redirect('index')


# перевод денег другому пользователю
# transfer_amount - сколько всего денег будет списано
# recipient_id - получатель перевода
def transaction(request, recipient_id: int, transfer_amount: float):
    accounts_sender = Account.objects.filter(owner=request.user)

    # создаем объект модели транзакции каждый раз
    Transaction.objects.create(sender_id=request.user.id, receiver_id=recipient_id)

    amount_money = transfer_amount / len(accounts_sender)  # количество денег, которое будет списано с каждого счета
    # пользователя

    # списываем деньги равномерно со счетов пользователя
    for account in accounts_sender:
        account.balance -= amount_money
        account.save()

    # получатель
    recipient = get_object_or_404(User, id=recipient_id)

    # отправляем деньги другому пользователю
