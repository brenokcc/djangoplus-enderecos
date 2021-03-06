# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-23 22:14


from django.db import migrations, models
import django.db.models.deletion
import djangoplus.db.models.fields
import enderecos.db.fields
import enderecos.migrations


class Migration(migrations.Migration):

    replaces = [('enderecos', '0001_initial'), ('enderecos', '0002_initial'), ('enderecos', '0003_delete_telefone'), ('enderecos', '0004_auto_20170503_1923'), ('enderecos', '0005_auto_20170503_2210'), ('enderecos', '0006_auto_20170605_2058')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bairro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Nome')),
                ('codigo', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='C\xf3digo')),
            ],
            options={
                'verbose_name': 'Bairro',
                'verbose_name_plural': 'Bairros',
            },
        ),
        migrations.CreateModel(
            name='Endereco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logradouro', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Logradouro')),
                ('numero', djangoplus.db.models.fields.IntegerField(verbose_name='N\xfamero')),
                ('complemento', djangoplus.db.models.fields.CharField(blank=True, max_length=255, null=True, verbose_name='Complemento')),
                ('cep', djangoplus.db.models.fields.CepField(blank=True, max_length=255, null=True, verbose_name='CEP')),
                ('bairro', djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enderecos.Bairro', verbose_name='Bairro')),
            ],
            options={
                'verbose_name': 'Endere\xe7o',
                'verbose_name_plural': 'Endere\xe7os',
            },
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Nome')),
                ('sigla', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Sigla')),
                ('codigo', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='C\xf3digo')),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Nome')),
                ('codigo', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='C\xf3digo')),
                ('estado', djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enderecos.Estado', verbose_name='Estado')),
            ],
            options={
                'verbose_name': 'Munic\xedpio',
                'verbose_name_plural': 'Munic\xedpios',
            },
        ),
        migrations.CreateModel(
            name='Regiao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Nome')),
                ('codigo', djangoplus.db.models.fields.CharField(max_length=255, verbose_name='C\xf3digo')),
            ],
            options={
                'verbose_name': 'Regi\xe3o',
                'verbose_name_plural': 'Regi\xf5es',
            },
        ),
        migrations.CreateModel(
            name='Telefone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', djangoplus.db.models.fields.CharField(choices=[('Residencial', 'Residencial'), ('Profissional', 'Profissional')], max_length=255, verbose_name='Tipo')),
                ('numero', djangoplus.db.models.fields.PhoneField(max_length=255, verbose_name='N\xfamero')),
            ],
            options={
                'verbose_name': 'Telefone',
                'verbose_name_plural': 'Telefones',
            },
        ),
        migrations.AddField(
            model_name='estado',
            name='regiao',
            field=djangoplus.db.models.fields.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.Regiao', verbose_name='Regi\xe3o'),
        ),
        migrations.AddField(
            model_name='endereco',
            name='municipio',
            field=djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enderecos.Municipio', verbose_name='Munic\xedpio'),
        ),
        migrations.AddField(
            model_name='bairro',
            name='cidade',
            field=djangoplus.db.models.fields.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enderecos.Municipio', verbose_name='Munic\xedpio'),
        ),
        migrations.RunPython(
            code=enderecos.migrations.load_fixture,
        ),
        migrations.DeleteModel(
            name='Telefone',
        ),
        migrations.RenameField(
            model_name='bairro',
            old_name='cidade',
            new_name='municipio',
        ),
        migrations.RemoveField(
            model_name='bairro',
            name='municipio',
        ),
        migrations.AlterField(
            model_name='endereco',
            name='bairro',
            field=djangoplus.db.models.fields.CharField(max_length=255, verbose_name='Bairro'),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=djangoplus.db.models.fields.CepField(default='', max_length=255, verbose_name='CEP'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Bairro',
        ),
        migrations.AlterField(
            model_name='endereco',
            name='cep',
            field=enderecos.db.fields.CepField(max_length=255, verbose_name='CEP'),
        ),
    ]
