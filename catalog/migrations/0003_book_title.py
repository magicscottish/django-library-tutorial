# Generated by Django 3.1.2 on 2020-10-26 23:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20201026_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='title',
            field=models.CharField(default='Title', max_length=200),
        ),
    ]
