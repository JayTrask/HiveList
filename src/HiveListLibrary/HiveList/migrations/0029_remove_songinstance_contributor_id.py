# Generated by Django 2.1.1 on 2018-11-27 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HiveList', '0028_merge_20181127_0257'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='songinstance',
            name='contributor_id',
        ),
    ]