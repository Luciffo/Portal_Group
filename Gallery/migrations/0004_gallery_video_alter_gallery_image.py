# Generated by Django 5.0.6 on 2024-06-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0003_alter_gallery_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='videos/'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
