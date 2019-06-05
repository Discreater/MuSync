# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artist(models.Model):
    sign_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=1024, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    location = models.CharField(max_length=1024, blank=True, null=True)
    familiarity = models.FloatField(blank=True, null=True)
    playmeid = models.IntegerField(blank=True, null=True)
    hotness = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artist'


class Song(models.Model):
    title = models.CharField(max_length=1024)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, null=True)
    release = models.CharField(max_length=1024, blank=True, null=True)
    release_id = models.IntegerField(blank=True, null=True)
    hotness = models.FloatField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    publish_year = models.IntegerField(blank=True, null=True)
    is_cached = models.IntegerField(default=0)
    has_lyric = models.IntegerField(default=0)
    yun_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'song'


class User(models.Model):
    name = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=45)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=45, blank=True, null=True)
    real_name = models.CharField(max_length=45, blank=True, null=True)
    gender = models.CharField(max_length=45, blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    signature = models.CharField(max_length=511, blank=True, null=True)
    is_online = models.IntegerField()
    is_stealth = models.IntegerField()
    friends = models.ManyToManyField('self', through='Friend', symmetrical=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'user'


class CollectionList(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    name = models.CharField(max_length=255)
    songs = models.ManyToManyField(Song, through='CollectionListHasSong')
    open_state = models.IntegerField(blank=True, null=True, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'collection_list'


class CollectionListHasSong(models.Model):
    collection_list = models.ForeignKey(CollectionList, models.DO_NOTHING)
    song = models.ForeignKey('Song', models.DO_NOTHING)
    add_time = models.DateTimeField()

    class Meta:
        db_table = 'collection_list_has_song'


class CurrentList(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    songs = models.ManyToManyField(Song, through='CurrentListHasSong')
    begin_time = models.DateTimeField()
    name = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        db_table = 'current_list'


class CurrentListHasSong(models.Model):
    current_list = models.ForeignKey(CurrentList, models.DO_NOTHING)
    song = models.ForeignKey('Song', models.DO_NOTHING)
    is_playing = models.IntegerField()
    order = models.IntegerField()
    play_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'current_list_has_song'


class Friend(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, related_name='from_user')
    friend = models.ForeignKey('User', models.DO_NOTHING, related_name='to_friend')
    begin_time = models.DateTimeField()
    musync_time = models.IntegerField(default=0)
    tag = models.CharField(max_length=1023, blank=True, null=True)
    remark = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        db_table = 'friend'


class Group(models.Model):
    creator = models.ForeignKey('User', models.DO_NOTHING, related_name='creator')
    current_user = models.ForeignKey('User', models.DO_NOTHING, related_name='current_user')
    name = models.CharField(max_length=45)
    create_time = models.DateTimeField()
    tag = models.CharField(max_length=1023, blank=True, null=True)
    users = models.ManyToManyField(User, through='GroupHasUser')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'group'


class GroupHasUser(models.Model):
    group = models.ForeignKey(Group, models.DO_NOTHING)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        db_table = 'group_has_user'
