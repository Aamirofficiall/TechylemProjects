# Generated by Django 3.0.2 on 2020-03-30 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TextExtract', '0002_remove_imagefile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagefile',
            name='image',
            field=models.ImageField(null=True, upload_to='MEDIA'),
        ),
    ]