# Generated by Django 2.2.1 on 2019-06-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musync_core', '0014_track_is_cached'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_online',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_stealth',
            field=models.IntegerField(default=0),
        ),
    ]