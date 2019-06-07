# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=1000, blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    location = models.TextField(blank=True, null=True)
    active_year_begin = models.DateTimeField(blank=True, null=True)
    active_year_end = models.DateTimeField(blank=True, null=True)
    associated_labels = models.TextField(blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    favorites = models.IntegerField(blank=True, null=True)
    members = models.TextField(blank=True, null=True)
    related_projects = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    wikipedia_page = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'artist'


class Album(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    released_date = models.DateTimeField(blank=True, null=True)
    engineer = models.TextField(blank=True, null=True)
    favorites = models.IntegerField(blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    listens = models.IntegerField(blank=True, null=True)
    producer = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    tracks = models.IntegerField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'album'


class Track(models.Model):
    title = models.CharField(max_length=1000, blank=True, null=True)
    artist = models.ForeignKey(Artist, models.DO_NOTHING, default=-1)
    album = models.ForeignKey(Album, models.DO_NOTHING, default=-1)
    set_split = models.TextField(blank=True, null=True)
    set_subset = models.TextField(blank=True, null=True)
    bit_rate = models.IntegerField(blank=True, null=True)
    comments = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(blank=True, null=True)
    recorded_date = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    favorites = models.IntegerField(blank=True, null=True)
    genre_top = models.TextField(blank=True, null=True)
    genres = models.TextField(blank=True, null=True)
    genres_all = models.TextField(blank=True, null=True)
    information = models.TextField(blank=True, null=True)
    interest = models.IntegerField(blank=True, null=True)
    language_code = models.TextField(blank=True, null=True)
    license = models.TextField(blank=True, null=True)
    listens = models.IntegerField(blank=True, null=True)
    lyricist = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    publisher = models.TextField(blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    is_short_cached = models.IntegerField(default=0)
    is_cached = models.IntegerField(default=0)
    has_lyric = models.IntegerField(default=0)
    yun_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'track'


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
    tracks = models.ManyToManyField(Track, through='CollectionListHasTrack')
    open_state = models.IntegerField(blank=True, null=True, default=1)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'collection_list'


class CollectionListHasTrack(models.Model):
    collection_list = models.ForeignKey(CollectionList, models.DO_NOTHING)
    track = models.ForeignKey('Track', models.DO_NOTHING)
    add_time = models.DateTimeField()

    class Meta:
        db_table = 'collection_list_has_track'


class CurrentList(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING)
    tracks = models.ManyToManyField(Track, through='CurrentListHasTrack')
    begin_time = models.DateTimeField()
    name = models.CharField(max_length=45, blank=True, null=True)
    is_active = models.IntegerField()

    class Meta:
        db_table = 'current_list'


class CurrentListHasTrack(models.Model):
    current_list = models.ForeignKey(CurrentList, models.DO_NOTHING)
    track = models.ForeignKey('Track', models.DO_NOTHING)
    is_playing = models.IntegerField()
    order = models.IntegerField()
    play_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'current_list_has_track'


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
