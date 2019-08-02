# Generated by Django 2.0.13 on 2019-07-17 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=' ', max_length=150, unique=True),
            preserve_default=False,
        ),
    ]
