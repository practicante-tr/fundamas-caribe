# Generated by Django 3.0.7 on 2021-12-28 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='comment_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogs.Comment'),
        ),
    ]