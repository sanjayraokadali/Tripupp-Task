# Generated by Django 3.0.3 on 2020-12-01 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0004_auto_20201201_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='LIVEClassModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=263)),
                ('subject', models.CharField(max_length=264)),
                ('date', models.CharField(max_length=264)),
                ('time', models.CharField(max_length=264)),
                ('query', models.TextField()),
            ],
        ),
    ]
