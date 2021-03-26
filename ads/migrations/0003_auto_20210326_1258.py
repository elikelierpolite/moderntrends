# Generated by Django 3.1.6 on 2021-03-26 10:58

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0002_ad_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='ad_url',
        ),
        migrations.CreateModel(
            name='AdFunnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200, null=True)),
                ('img', models.TextField()),
                ('theme', models.CharField(max_length=200, null=True)),
                ('cta', models.CharField(max_length=200, null=True)),
                ('url', models.TextField()),
                ('p_img', models.TextField()),
                ('description_title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('body', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('ad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ads.ad')),
            ],
        ),
    ]
