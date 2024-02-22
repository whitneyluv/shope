# Generated by Django 4.2 on 2024-02-13 11:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profile_app', '0003_profile_created_at_profile_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='profiles/<function Profile.get_email at 0x7f27d83f8b80>/%Y/%m/%d', verbose_name='profile avatar'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('name', models.CharField(max_length=20, unique=True, verbose_name='Name')),
                ('logo', models.ImageField(blank=True, upload_to='seller/<function Seller.get_email at 0x7f27d83f8f40>/%Y/%m/%d', verbose_name='Logotype')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
