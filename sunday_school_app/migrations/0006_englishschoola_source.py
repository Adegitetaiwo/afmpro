# Generated by Django 3.0.3 on 2020-04-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday_school_app', '0005_auto_20200411_1800'),
    ]

    operations = [
        migrations.AddField(
            model_name='englishschoola',
            name='source',
            field=models.FileField(default=True, max_length=500, upload_to='media'),
            preserve_default=False,
        ),
    ]
