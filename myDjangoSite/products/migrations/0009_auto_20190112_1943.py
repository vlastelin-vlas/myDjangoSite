# Generated by Django 2.1.5 on 2019-01-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20190111_2026'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='productimage',
            name='is_main',
            field=models.BooleanField(default=False),
        ),
    ]
