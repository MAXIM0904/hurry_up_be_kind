# Generated by Django 4.0.3 on 2022-04-20 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('all_users', '0004_remove_philantropist_status_remove_ward_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='philantropist',
            name='about_me_philantropist',
            field=models.TextField(blank=True, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='ward',
            name='about_me_ward',
            field=models.TextField(blank=True, verbose_name='О себе'),
        ),
    ]
