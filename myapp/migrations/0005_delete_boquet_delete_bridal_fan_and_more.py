# Generated by Django 4.1.2 on 2022-10-20 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_bakery_product_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Boquet',
        ),
        migrations.DeleteModel(
            name='Bridal_Fan',
        ),
        migrations.DeleteModel(
            name='Dowry_Wrapping',
        ),
        migrations.DeleteModel(
            name='Souvenirs',
        ),
        migrations.AlterField(
            model_name='bakery',
            name='product_image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
