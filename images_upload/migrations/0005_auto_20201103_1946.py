# Generated by Django 3.1.2 on 2020-11-03 19:46

from django.db import migrations, models
import images_upload.models


class Migration(migrations.Migration):

    dependencies = [
        ('images_upload', '0004_auto_20201103_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(upload_to=images_upload.models.path_file),
        ),
    ]
