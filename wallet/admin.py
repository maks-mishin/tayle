from django.contrib import admin

from .models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'balance', 'created_date')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'value', 'created_date', 'sender', 'receiver')


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
