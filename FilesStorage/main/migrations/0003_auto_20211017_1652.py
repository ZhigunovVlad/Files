# Generated by Django 3.2.8 on 2021-10-17 13:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc




class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20211015_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='details',
            field=models.TextField(default='Тестовое описание', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='file',
            name='size',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='file',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 17, 13, 52, 15, 376233, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='file',
            name='title',
            field=models.CharField(default='', max_length=30),
        ),
    ]
