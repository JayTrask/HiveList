# Generated by Django 2.1.2 on 2018-12-03 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HiveList', '0004_songinstance_num_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='num_vote',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='num_vote_down',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='num_vote_up',
            field=models.PositiveIntegerField(db_index=True, default=0),
        ),
        migrations.AddField(
            model_name='song',
            name='vote_score',
            field=models.IntegerField(db_index=True, default=0),
        ),
    ]
