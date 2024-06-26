# Generated by Django 4.2.11 on 2024-05-06 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_about', '0010_alter_aboutinfo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.IntegerField(default=0)),
            ],
        ),
    ]
