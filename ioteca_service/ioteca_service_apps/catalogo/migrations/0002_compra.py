# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-30 16:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cantidad', models.IntegerField()),
                ('distribuidor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Distribuidor')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Empresa')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.Producto')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Compras',
                'verbose_name': 'Compra',
            },
        ),
    ]
