# Generated by Django 4.2.11 on 2024-05-06 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_testimonials', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='galerie/'),
        ),
    ]
