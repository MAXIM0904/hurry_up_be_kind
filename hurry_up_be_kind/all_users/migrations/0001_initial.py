# Generated by Django 4.0.3 on 2022-04-21 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me_ward', models.TextField(blank=True, verbose_name='О себе')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Номер телефона')),
                ('registrarion_date_ward', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('address_ward', models.TextField(default='', verbose_name='Адрес проживания')),
                ('user_profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_ward', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Philantropist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me_philantropist', models.TextField(blank=True, verbose_name='О себе')),
                ('size_donations', models.IntegerField(default=0, verbose_name='Размер пожертвований')),
                ('phone', models.CharField(blank=True, max_length=20, verbose_name='Номер телефона')),
                ('registrarion_date_philantropist', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('user_profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_philantropist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
