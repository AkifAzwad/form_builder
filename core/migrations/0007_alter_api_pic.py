# Generated by Django 4.0.3 on 2022-03-13 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_api_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='api',
            name='pic',
            field=models.ImageField(upload_to='images'),
        ),
    ]
