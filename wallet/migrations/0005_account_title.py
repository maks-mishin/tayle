# Generated by Django 3.2.7 on 2021-09-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_auto_20210917_0925'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='title',
            field=models.CharField(default='New account', max_length=255),
        ),
    ]
