# Generated by Django 3.0.3 on 2020-04-16 21:43

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sunday_school_app', '0007_auto_20200411_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='elementaryschool',
            name='source',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='englishschoola',
            name='source',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='englishschooli',
            name='source',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='frenchschoola',
            name='source',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='frenchschooli',
            name='source',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='yorubaschoola',
            name='source',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
        migrations.AlterField(
            model_name='yorubaschooli',
            name='source',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]
