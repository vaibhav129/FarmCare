# Generated by Django 3.2.5 on 2021-11-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_auction_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='category',
            field=models.CharField(choices=[('Fruits', 'Fruits'), ('vegetable', 'Vegetable'), ('LandEquipment', 'Land Equipment'), ('RentLand', 'Rent Land'), ('other', 'other')], default='Fruits', max_length=60),
        ),
        migrations.AlterField(
            model_name='closebid',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]