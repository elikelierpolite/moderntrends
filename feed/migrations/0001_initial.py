# Generated by Django 3.1.6 on 2021-03-29 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('headline', models.CharField(blank=True, max_length=200, null=True)),
                ('img', models.CharField(blank=True, max_length=200, null=True)),
                ('hook', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('body2', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(unique=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date published')),
                ('category', models.CharField(choices=[('BreakingNews', 'BreakingNews'), ('Sports', 'Sports'), ('Health', 'Health'), ('Politics', 'Politics'), ('Business', 'Business'), ('ADVERT', 'Advert')], default='BreakingNews', max_length=200)),
                ('is_ad', models.BooleanField()),
                ('cta', models.CharField(blank=True, max_length=500, null=True)),
                ('theme', models.CharField(blank=True, max_length=500, null=True)),
                ('ad_url', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Celebrity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('headline', models.CharField(max_length=200, null=True)),
                ('img', models.TextField(null=True)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Discover',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('discover_text', models.CharField(max_length=200, null=True)),
                ('discover_hook', models.CharField(max_length=200, null=True)),
                ('discover_img', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('hook', models.CharField(blank=True, max_length=200, null=True)),
                ('is_ad', models.BooleanField(default=False)),
                ('cta', models.CharField(blank=True, max_length=200, null=True)),
                ('url', models.CharField(blank=True, max_length=200, null=True)),
                ('up_next_title', models.CharField(max_length=200, null=True)),
                ('up_next_img', models.TextField(null=True)),
                ('up_next_url', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Finance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('headline', models.CharField(max_length=200, null=True)),
                ('img', models.TextField(null=True)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Future',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('headline', models.CharField(max_length=200, null=True)),
                ('img', models.TextField(null=True)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('headline', models.CharField(max_length=200, null=True)),
                ('img', models.TextField(null=True)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('price', models.CharField(max_length=200, null=True)),
                ('cta', models.CharField(max_length=200, null=True)),
                ('url', models.CharField(max_length=200, null=True)),
                ('theme', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productotd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('img', models.TextField(null=True)),
                ('price', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('cta', models.CharField(max_length=200, null=True)),
                ('url', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Topten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('list_headline', models.CharField(max_length=200, null=True)),
                ('list_img', models.TextField(null=True)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('headline', models.CharField(max_length=200, null=True)),
                ('thumbnail', models.TextField(null=True)),
                ('slug', models.SlugField(unique=True)),
                ('video', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('headline', models.CharField(max_length=200, null=True)),
                ('img', models.TextField(null=True)),
                ('slug', models.SlugField(unique=True)),
                ('body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_title', models.CharField(max_length=200, null=True)),
                ('item_content', models.TextField(blank=True, null=True)),
                ('item_content_img', models.TextField(blank=True, null=True)),
                ('topten', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.topten')),
            ],
        ),
        migrations.CreateModel(
            name='DiscoverPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discover_title', models.CharField(max_length=200)),
                ('discover_img', models.TextField()),
                ('discover', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='feed.discover')),
            ],
        ),
    ]
