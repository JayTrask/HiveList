# Generated by Django 2.1.3 on 2018-11-27 01:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HiveList', '0025_playlist_playlist_creator_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='playlist',
            options={'permissions': (('can_contribute', 'Contribute songs'),)},
        ),
    ]
