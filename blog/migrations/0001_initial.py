# Generated by Django 3.1.6 on 2021-03-21 14:13

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200, null=True)),
                ('img', models.TextField(null=True)),
                ('hook', models.TextField(null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
            ],
        ),
    ]
