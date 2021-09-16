# Generated by Django 3.2.7 on 2021-09-16 09:12

from decimal import Decimal
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, max_digits=9, validators=[django.core.validators.MinValueValidator(Decimal('0.00'))])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]