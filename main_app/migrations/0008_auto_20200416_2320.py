# Generated by Django 3.0.3 on 2020-04-16 21:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_sm_phone_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='displaysilder',
            name='displayImage',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]