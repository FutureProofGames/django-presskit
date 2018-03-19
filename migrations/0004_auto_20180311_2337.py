# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-11 23:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_presskit', '0003_auto_20180311_2321'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='quotes',
            field=models.ManyToManyField(blank=True, to='django_presskit.Quote'),
        ),
        migrations.AddField(
            model_name='project',
            name='quotes',
            field=models.ManyToManyField(blank=True, to='django_presskit.Quote'),
        ),
        migrations.AlterField(
            model_name='additionallink',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='award',
            name='info',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='additional_links',
            field=models.ManyToManyField(blank=True, to='django_presskit.AdditionalLink'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='credit',
            name='role',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='credit',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='platform',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='additional_links',
            field=models.ManyToManyField(blank=True, to='django_presskit.AdditionalLink'),
        ),
        migrations.AlterField(
            model_name='project',
            name='credits',
            field=models.ManyToManyField(blank=True, to='django_presskit.Credit'),
        ),
    ]
