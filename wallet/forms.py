from decimal import Decimal

from django import forms
from django.core.validators import MinValueValidator

from users.models import User
from wallet.models import Account


class AccountForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=True,
        label='Введите название счета')
    balance = forms.DecimalField(
        required=True,
        label='Введите баланс счета'
    )

    title.widget.attrs.update({'class': 'form-control'})
    balance.widget.attrs.update({'class': 'form-control'})


class TransactionForm(forms.Form):
    CHOICES = tuple((x.id, f'{x.title} ({x.owner})') for x in Account.objects.all())

    accounts = forms.MultipleChoiceField(
        choices=CHOICES,
        required=True,
        label='Выберите счета списания'
    )

    recipient = forms.ChoiceField(
        choices=CHOICES,
        required=True,
        label='Выберите счет получателя')

    value = forms.DecimalField(
        required=True,
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))],
        label='Сумма'
    )

    recipient.widget.attrs.update({'class': 'form-control'})
    accounts.widget.attrs.update({'class': 'form-control'})
    value.widget.attrs.update({'class': 'form-control'})
