# Generated by Django 2.1.5 on 2019-01-09 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
