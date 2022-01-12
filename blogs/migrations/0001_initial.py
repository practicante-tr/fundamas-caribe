# Generated by Django 3.0.7 on 2021-12-28 03:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Fecha de Creacion')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
                'ordering': ['id'],
            },
        ),
    ]