# Generated by Django 2.0.2 on 2018-03-26 10:59

import catalog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20180326_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=catalog.models.Book.get_image_name),
        ),
    ]
