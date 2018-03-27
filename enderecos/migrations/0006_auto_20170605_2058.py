# -*- coding: utf-8 -*-

# Generated by Django 1.11 on 2017-06-05 20:58


from django.db import migrations
import enderecos.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0005_auto_20170503_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=enderecos.db.fields.CepField(max_length=255, verbose_name='CEP'),
        ),
    ]
