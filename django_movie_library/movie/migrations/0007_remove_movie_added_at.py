# Generated by Django 3.1.2 on 2022-03-24 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0006_auto_20220324_1435'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='added_at',
        ),
    ]
