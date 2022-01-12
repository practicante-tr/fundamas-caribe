# Generated by Django 3.0.7 on 2021-12-28 04:24

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor.fields.RichTextField()),
                ('autor', models.CharField(max_length=150, verbose_name='Autor')),
                ('email', models.CharField(max_length=150, verbose_name='Correo')),
                ('web_link', models.URLField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comment',
                'ordering': ['id'],
            },
        ),
    ]
