# Generated by Django 5.0.6 on 2024-06-29 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gallery', '0004_gallery_video_alter_gallery_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gallery',
            old_name='titel',
            new_name='title',
        ),
    ]
