# Generated by Django 4.0.1 on 2022-01-13 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stuff',
            name='size',
            field=models.CharField(default='small', max_length=100, verbose_name='Размер'),
        ),
    ]
