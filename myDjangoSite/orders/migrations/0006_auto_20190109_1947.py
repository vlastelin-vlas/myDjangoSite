# Generated by Django 2.1.5 on 2019-01-09 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20190109_1849'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=20, null=True)),
            ],
            options={
                'verbose_name': 'Status',
                'verbose_name_plural': 'Statuses',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='orders.Status'),
        ),
    ]