# Generated by Django 3.0.1 on 2020-01-07 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0005_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='oreg',
            name='status',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='ureg',
            name='status',
            field=models.CharField(default='', max_length=20),
        ),
    ]