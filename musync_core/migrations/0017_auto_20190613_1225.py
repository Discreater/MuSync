# Generated by Django 2.2.1 on 2019-06-13 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musync_core', '0016_auto_20190612_0015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentlist',
            name='begin_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='currentlist',
            name='is_active',
            field=models.IntegerField(default=1),
        ),
    ]
