# -*- coding: utf-8 -*-

# Generated by Django 1.11 on 2017-05-03 19:06


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0002_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Telefone',
        ),
    ]
