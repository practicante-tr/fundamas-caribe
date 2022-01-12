# Generated by Django 3.0.7 on 2021-12-31 17:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_auto_20211231_0934'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=50, verbose_name='Email')),
                ('subs_date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Date of Subscription')),
            ],
            options={
                'verbose_name': 'Subscription',
                'verbose_name_plural': 'Subscriptions',
                'db_table': 'subscriptions',
                'ordering': ['id'],
            },
        ),
    ]