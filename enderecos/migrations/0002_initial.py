# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 18:12
from __future__ import unicode_literals
from django.core.management import call_command
from django.db import migrations
import os


def load_fixture(apps, schema_editor):
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    file_path = os.path.join(base_dir, 'fixtures/initial_data.json.zip')
    call_command('loaddata', file_path)


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
