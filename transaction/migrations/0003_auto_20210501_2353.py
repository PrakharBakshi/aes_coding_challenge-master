# Generated by Django 3.1.5 on 2021-05-01 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_auto_20210501_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_number',
            field=models.CharField(max_length=10),
        ),
    ]
