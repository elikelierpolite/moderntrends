# Generated by Django 3.1.6 on 2021-03-28 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
