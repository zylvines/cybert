# Generated by Django 5.0.6 on 2024-05-30 04:28

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber', '0002_alter_gamer_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='updates_news',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
