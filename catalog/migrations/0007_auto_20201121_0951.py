# Generated by Django 3.1.2 on 2020-11-21 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_auto_20201119_1145'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_edit_authors', 'Can edit authors'),)},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'permissions': (('can_edit_books', 'Can edit books'),)},
        ),
    ]