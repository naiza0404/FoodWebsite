# Generated by Django 4.2.1 on 2023-09-02 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_cart_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=200)),
                ('price', models.CharField(default='', max_length=255)),
            ],
        ),
    ]
