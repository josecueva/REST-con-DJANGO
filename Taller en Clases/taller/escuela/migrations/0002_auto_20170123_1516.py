# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='estudiante',
            old_name='code',
            new_name='apellido',
        ),
        migrations.RenameField(
            model_name='estudiante',
            old_name='title',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='language',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='style',
        ),
        migrations.AddField(
            model_name='estudiante',
            name='cedula',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='ciudad',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='estudiante',
            name='provincia',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
