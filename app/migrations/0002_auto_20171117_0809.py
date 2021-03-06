# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-17 08:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationPosition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('type', models.CharField(choices=[('F', 'FACULTY'), ('A', 'ADMIN'), ('M', 'MODERATOR')], default='M', max_length=1, verbose_name='position type')),
                ('description', models.CharField(blank=True, max_length=256, null=True, verbose_name='position description')),
            ],
            options={
                'verbose_name': 'organization positions',
                'verbose_name_plural': 'organization positions',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='organization',
            name='abbr',
            field=models.CharField(blank=True, default='', max_length=10, null=True, unique=True, verbose_name='abbreviation'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(default='', verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='organization email'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='end_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='date ended'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='found_date',
            field=models.DateTimeField(verbose_name='date founded'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='deleted'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='is public'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='last modified'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='logo'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='members',
            field=models.IntegerField(default=0, verbose_name='number of members'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='name'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='summary',
            field=models.TextField(default='', max_length=256, verbose_name='summary'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='breadth',
            field=models.CharField(choices=[('B', 'BROAD'), ('S', 'SPECIFIC'), ('N', 'NICHE')], default='N', max_length=1, verbose_name='breadth'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='tag'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='parents',
            field=models.ManyToManyField(blank=True, to='app.Tag'),
        ),
        migrations.AddField(
            model_name='organizationposition',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Organization'),
        ),
    ]
