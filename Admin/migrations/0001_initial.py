# Generated by Django 3.0.1 on 2020-01-02 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ureg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('hname', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('pin', models.IntegerField()),
                ('lmark', models.CharField(max_length=20)),
                ('phone', models.IntegerField()),
                ('uname', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=20)),
            ],
        ),
    ]