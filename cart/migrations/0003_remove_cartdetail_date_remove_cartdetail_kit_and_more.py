# Generated by Django 5.0.2 on 2024-03-15 13:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apply', '0005_alter_apply_apply_status'),
        ('cart', '0002_alter_cartdetail_date_alter_cartdetail_kit_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartdetail',
            name='date',
        ),
        migrations.RemoveField(
            model_name='cartdetail',
            name='kit',
        ),
        migrations.RemoveField(
            model_name='cartdetail',
            name='lecture',
        ),
        migrations.RemoveField(
            model_name='cartdetail',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='cartdetail',
            name='time',
        ),
        migrations.AddField(
            model_name='cartdetail',
            name='apply',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='apply.apply'),
            preserve_default=False,
        ),
    ]
