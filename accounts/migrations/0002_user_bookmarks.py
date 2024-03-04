# Generated by Django 3.2.13 on 2024-03-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_bookmark'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(related_name='bookmarked_by', to='community.Post'),
        ),
    ]