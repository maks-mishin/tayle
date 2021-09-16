from django.urls import path

from . import views
from .views import my_accounts, create_wallet, all_accounts, account_detail

urlpatterns = [
    path('', my_accounts, name='index'),
    path('new/', create_wallet, name='create_wallet'),
    path('accounts/all/', all_accounts, name='all_accounts'),
    path('accounts/<int:account_id>', account_detail, name="account_detail")
]
