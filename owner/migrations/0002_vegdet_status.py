# Generated by Django 3.0.1 on 2020-01-14 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vegdet',
            name='status',
            field=models.CharField(default='', max_length=20),
        ),
    ]
