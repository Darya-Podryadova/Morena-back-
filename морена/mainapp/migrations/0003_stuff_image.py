# Generated by Django 4.0.1 on 2022-01-13 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_stuff_size'),
    ]

    operations = [
        migrations.AddField(
            model_name='stuff',
            name='image',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
