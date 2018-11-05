# Generated by Django 2.1.3 on 2018-11-05 20:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('HiveList', '0022_auto_20181104_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songinstance',
            name='song_instance_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID for this particular Song Instance', primary_key=True, serialize=False),
        ),
    ]
