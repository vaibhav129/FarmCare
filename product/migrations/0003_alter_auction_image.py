# Generated by Django 3.2.5 on 2021-11-07 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
