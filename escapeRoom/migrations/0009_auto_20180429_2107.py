# Generated by Django 2.0.4 on 2018-04-29 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escapeRoom', '0008_auto_20180423_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='content',
            field=models.ImageField(blank=True, default=None, upload_to=''),
        ),
    ]
