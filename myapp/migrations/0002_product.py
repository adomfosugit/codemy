# Generated by Django 4.1.1 on 2022-10-03 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Product name')),
                ('Description', models.CharField(max_length=300, verbose_name='Description')),
                ('Price', models.FloatField(default=1.0, verbose_name=' price')),
                ('product_image', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
