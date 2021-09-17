from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models

from users.models import User


class Account(models.Model):
    title = models.CharField(max_length=255, default='New account')
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='accounts'
    )
    # баланс везде будет в рублях
    balance = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )

    class Meta:
        ordering = ("-created_date",)


class Transaction(models.Model):
    value = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )

    created_date = models.DateTimeField(
        auto_now_add=True,
        db_index=True,
    )

    receiver = models.ForeignKey(
        Account,
        related_name='receiver',
        on_delete=models.PROTECT,
        default=''
    )

    sender = models.ForeignKey(
        User,
        related_name='creator',
        on_delete=models.PROTECT,
        default=''
    )

    class Meta:
        ordering = ("-created_date",)
