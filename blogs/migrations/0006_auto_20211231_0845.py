# Generated by Django 3.0.7 on 2021-12-31 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0005_auto_20211228_0003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comment',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
