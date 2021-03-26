# Generated by Django 3.1.6 on 2021-03-26 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_text', models.CharField(max_length=200, null=True)),
                ('story_img', models.TextField(null=True)),
                ('slug', models.SlugField(unique=True)),
                ('is_ad', models.BooleanField()),
                ('ad_url', models.TextField(blank=True, null=True)),
                ('ad_cta', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('story_title', models.CharField(max_length=200, null=True)),
                ('story_img', models.TextField(null=True)),
                ('up_next_title', models.CharField(max_length=200, null=True)),
                ('up_next_img', models.TextField(null=True)),
                ('up_next_url', models.CharField(max_length=200, null=True)),
                ('story', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feedstory.story')),
            ],
        ),
    ]
