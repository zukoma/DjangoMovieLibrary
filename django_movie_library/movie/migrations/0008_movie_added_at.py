# Generated by Django 3.1.2 on 2022-03-24 13:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_remove_movie_added_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='added_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
