# Generated by Django 4.2.11 on 2024-05-05 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_skills', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='percentage',
        ),
        migrations.AddField(
            model_name='skill',
            name='level',
            field=models.IntegerField(default=0),
        ),
    ]