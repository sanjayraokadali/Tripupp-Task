# Generated by Django 3.0.3 on 2020-11-30 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClarifyDoubtModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=264)),
                ('subject', models.CharField(max_length=264)),
                ('doubt_pic', models.ImageField(upload_to='pics')),
                ('doubt', models.TextField()),
            ],
        ),
    ]
