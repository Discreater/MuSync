# Generated by Django 2.2.1 on 2019-06-15 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musync_core', '0019_track_short_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='currentlisthastrack',
            name='is_short',
            field=models.IntegerField(default=0),
        ),
    ]
