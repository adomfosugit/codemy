# Generated by Django 4.1.1 on 2022-10-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_bridal_fan_dowry_wrapping_souvenirs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bakery',
            name='product_image',
            field=models.ImageField(null=True, upload_to='bridalfan/images/'),
        ),
    ]
