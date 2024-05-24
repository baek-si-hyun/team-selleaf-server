# Generated by Django 5.0.2 on 2024-03-13 11:05

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0002_alter_memberaddress_address_detail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alarm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('alarm_status', models.BooleanField(default=False)),
                ('alarm_category', models.IntegerField()),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='receiver', to='member.member')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sender', to='member.member')),
            ],
            options={
                'db_table': 'tbl_alarm',
            },
        ),
    ]