# Generated by Django 2.2 on 2019-06-01 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_item',
            name='size',
        ),
        migrations.RemoveField(
            model_name='add_item',
            name='type',
        ),
    ]
