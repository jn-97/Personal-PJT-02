# Generated by Django 3.2.13 on 2024-02-22 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0004_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.IntegerField(default=0),
        ),
    ]
