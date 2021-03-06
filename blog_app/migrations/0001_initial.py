# Generated by Django 3.0.3 on 2020-04-13 12:55

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blogTitle', models.CharField(max_length=50, verbose_name='Blog Tile')),
                ('blogSubtile', models.TextField(blank=True, null=True, verbose_name='Subtitle[if any]')),
                ('featuredImage', models.ImageField(upload_to='images', verbose_name='Featured Image')),
                ('likeCount', models.IntegerField(blank=True, null=True)),
                ('blogBody', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Body')),
                ('username', models.CharField(max_length=100)),
                ('userPicture', models.ImageField(upload_to='images')),
                ('aboutUser', ckeditor.fields.RichTextField()),
                ('time', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_app.blog')),
            ],
        ),
    ]
