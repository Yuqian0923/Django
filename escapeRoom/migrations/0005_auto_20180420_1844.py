# Generated by Django 2.0.4 on 2018-04-20 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escapeRoom', '0004_userdata_players'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mission',
            name='mission_id',
        ),
        migrations.AddField(
            model_name='player',
            name='mission_id',
            field=models.IntegerField(default=-1),
        ),
    ]
