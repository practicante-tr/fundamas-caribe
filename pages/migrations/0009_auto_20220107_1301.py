# Generated by Django 3.0.7 on 2022-01-07 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20220107_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(verbose_name='Mensaje'),
        ),
    ]
