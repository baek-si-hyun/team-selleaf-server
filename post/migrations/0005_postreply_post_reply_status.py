# Generated by Django 5.0.2 on 2024-05-17 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_alter_posttag_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='postreply',
            name='post_reply_status',
            field=models.IntegerField(choices=[(0, '비활성화'), (1, '활성화')], default=1),
        ),
    ]
