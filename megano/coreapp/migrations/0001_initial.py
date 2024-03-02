# Generated by Django 4.2 on 2024-02-29 16:51

import coreapp.utils.images_directory_path
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('title1', models.CharField(blank=True, max_length=30, null=True, verbose_name='banner_title1')),
                ('title2', models.CharField(blank=True, max_length=30, null=True, verbose_name='banner_title2')),
                ('title3', models.CharField(blank=True, max_length=30, null=True, verbose_name='banner_title3')),
                ('text', models.TextField(blank=True, max_length=200, null=True, verbose_name='banner_text')),
                ('button', models.CharField(blank=True, default='Get Started', max_length=30, null=True, verbose_name='banner_footer')),
                ('image', models.ImageField(blank=True, null=True, upload_to=coreapp.utils.images_directory_path.banner_images_directory_path, verbose_name='banner_image')),
                ('link', models.URLField(blank=True, null=True, verbose_name='banner_link')),
            ],
            options={
                'verbose_name': 'Banner',
                'verbose_name_plural': 'Banners',
            },
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='creation time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated time')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('key', models.CharField(max_length=255, unique=True, verbose_name='key')),
                ('value', models.TextField(verbose_name='value')),
            ],
            options={
                'verbose_name': 'Setting',
                'verbose_name_plural': 'Settings',
            },
        ),
    ]
