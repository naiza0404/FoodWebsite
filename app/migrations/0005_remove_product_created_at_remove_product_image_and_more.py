# Generated by Django 4.2.1 on 2023-08-31 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_admin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
