# Generated by Django 4.2.7 on 2023-11-18 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(blank=True, upload_to='user_images', verbose_name='Фотография'),
        ),
    ]
