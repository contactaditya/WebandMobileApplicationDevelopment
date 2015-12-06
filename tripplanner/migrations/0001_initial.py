# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('mobilenumber', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
                ('confirmpassword', models.CharField(max_length=100)),
                ('dateofbirth', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=100)),
                ('bar', models.CharField(max_length=100, default=False)),
                ('coffee', models.CharField(max_length=100, default=False)),
                ('restaurant', models.CharField(max_length=100, default=False)),
                ('food', models.CharField(max_length=100)),
                ('art', models.CharField(max_length=100, default=False)),
                ('fashion', models.CharField(max_length=100, default=False)),
                ('film', models.CharField(max_length=100, default=False)),
                ('holiday', models.CharField(max_length=100, default=False)),
                ('music', models.CharField(max_length=100, default=False)),
                ('shopping', models.CharField(max_length=100, default=False)),
                ('sport', models.CharField(max_length=100, default=False)),
                ('outdoor', models.CharField(max_length=100, default=False)),
                ('acti', models.CharField(max_length=100)),
                ('trend', models.CharField(max_length=100, default=False)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
