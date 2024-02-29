# Generated by Django 4.2 on 2024-02-21 15:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0004_remove_user_is_activation_key_expires_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='middle_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='activation_key_will_expires',
            field=models.DateField(default=datetime.date(2024, 2, 23), verbose_name='date of creation activation key'),
        ),
    ]