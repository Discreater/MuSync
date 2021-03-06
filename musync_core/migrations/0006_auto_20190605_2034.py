# Generated by Django 2.2.1 on 2019-06-05 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musync_core', '0005_auto_20190602_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='sign_id',
        ),
        migrations.AlterField(
            model_name='artist',
            name='location',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.TextField(blank=True, max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.TextField(max_length=1024),
        ),
    ]
