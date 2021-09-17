from django.urls import path

from . import views
from .views import my_accounts, create_account, all_accounts, \
    account_detail, delete_account, transfer, all_transfers

urlpatterns = [
    path('', my_accounts, name='index'),
    path('new/', create_account, name='create_account'),
    path('accounts/all/', all_accounts, name='all_accounts'),
    path('accounts/<int:account_id>', account_detail, name="account_detail"),
    path('accounts/delete/<int:account_id>', delete_account, name='delete_account'),
    path('transfer/', transfer, name='transfer'),
    path('transfer/all', all_transfers, name='transfers')
]
