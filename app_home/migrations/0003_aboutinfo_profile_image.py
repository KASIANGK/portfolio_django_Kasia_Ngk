# Generated by Django 4.2.11 on 2024-05-05 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home', '0002_aboutinfo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutinfo',
            name='profile_image',
            field=models.ImageField(default='default_profile.jpg', upload_to='galerie/'),
        ),
    ]
