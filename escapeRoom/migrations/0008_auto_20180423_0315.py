# Generated by Django 2.0.4 on 2018-04-23 03:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escapeRoom', '0007_auto_20180423_0259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mission',
            old_name='game_id',
            new_name='gameid',
        ),
    ]