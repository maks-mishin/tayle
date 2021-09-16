from django import forms


class AccountForm(forms.Form):
    balance = forms.DecimalField(label='Введите баланс счета')
    balance.widget.attrs.update(
        {
            'class': 'form-control',
        }
    )