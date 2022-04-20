# Generated by Django 4.0.3 on 2022-04-12 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


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
                ('about_me_ward', models.TextField(verbose_name='О себе')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('registrarion_date_ward', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('address_ward', models.TextField(default='', verbose_name='Адрес проживания')),
                ('user_profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_ward', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Philantropist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me_philantropist', models.TextField(verbose_name='О себе')),
                ('size_donations', models.IntegerField(default=0, verbose_name='Размер пожертвований')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('registrarion_date_philantropist', models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации')),
                ('user_profile', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile_philantropist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]