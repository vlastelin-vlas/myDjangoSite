# Generated by Django 2.1.5 on 2019-01-09 15:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='status',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='status',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
