# Generated by Django 3.1.2 on 2022-03-24 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.CharField(default=10, max_length=100),
            preserve_default=False,
        ),
    ]