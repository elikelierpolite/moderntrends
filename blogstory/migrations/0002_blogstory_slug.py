# Generated by Django 3.1.6 on 2021-03-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogstory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogstory',
            name='slug',
            field=models.SlugField(default='hey', unique=True),
            preserve_default=False,
        ),
    ]
