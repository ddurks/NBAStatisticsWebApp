# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class NbastatsPlayerinfo(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()
    college = models.CharField(max_length=250)
    born = models.IntegerField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    image = models.TextField()

    class Meta:
        managed = False
        db_table = 'nbastats_playerinfo'


class NbastatsSeasonstats(models.Model):
    position = models.CharField(max_length=10)
    age = models.IntegerField()
    year = models.IntegerField()
    team = models.CharField(max_length=10)
    g = models.IntegerField()
    gs = models.IntegerField()
    mp = models.IntegerField()
    per = models.FloatField()
    tspct = models.FloatField()
    threepar = models.FloatField()
    ftr = models.FloatField()
    orbpct = models.FloatField()
    drbpct = models.FloatField()
    trbpct = models.FloatField()
    astpct = models.FloatField()
    stlpct = models.FloatField()
    tovpct = models.FloatField()
    usgpct = models.FloatField()
    ows = models.FloatField()
    dws = models.FloatField()
    ws = models.FloatField()
    ws_48 = models.FloatField()
    obpm = models.FloatField()
    dbpm = models.FloatField()
    bpm = models.FloatField()
    vorp = models.FloatField()
    fg = models.IntegerField()
    fga = models.IntegerField()
    fgpct = models.FloatField()
    threep = models.IntegerField()
    threepa = models.IntegerField()
    threeppct = models.FloatField()
    twop = models.IntegerField()
    twopa = models.IntegerField()
    twoppct = models.FloatField()
    efgpct = models.FloatField()
    ft = models.IntegerField()
    ftpct = models.FloatField()
    orb = models.IntegerField()
    drb = models.IntegerField()
    trb = models.IntegerField()
    ast = models.IntegerField()
    stl = models.IntegerField()
    blk = models.IntegerField()
    tov = models.IntegerField()
    pf = models.IntegerField()
    pts = models.IntegerField()
    player = models.ForeignKey(NbastatsPlayerinfo, models.DO_NOTHING, blank=True, null=True)
    blkpct = models.FloatField()
    fta = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'nbastats_seasonstats'


class NbastatsTeaminfo(models.Model):
    abbreviation = models.CharField(max_length=3)
    city = models.CharField(max_length=50)
    mascot = models.CharField(max_length=50)
    founded = models.IntegerField()
    championships = models.CharField(max_length=250)
    logo = models.TextField()

    class Meta:
        managed = False
        db_table = 'nbastats_teaminfo'
