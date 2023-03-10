# Generated by Django 4.1.5 on 2023-01-12 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='label',
            field=models.CharField(max_length=52, unique=True, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(max_length=52, unique=True, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='place',
            name='label',
            field=models.CharField(max_length=52, unique=True, verbose_name='Label'),
        ),
    ]
