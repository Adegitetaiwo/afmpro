# Generated by Django 3.0.3 on 2020-04-07 04:51

from django.db import migrations, models
import sunday_school_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('sunday_school_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frenchschooli',
            name='Topic',
        ),
        migrations.RemoveField(
            model_name='frenchschooli',
            name='active',
        ),
        migrations.RemoveField(
            model_name='frenchschooli',
            name='bibleText',
        ),
        migrations.RemoveField(
            model_name='frenchschooli',
            name='body',
        ),
        migrations.RemoveField(
            model_name='frenchschooli',
            name='comment',
        ),
        migrations.AlterField(
            model_name='frenchschooli',
            name='lessonNumber',
            field=models.IntegerField(verbose_name=sunday_school_app.models.yorubaSchoolA),
        ),
    ]
