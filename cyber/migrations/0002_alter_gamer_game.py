# Generated by Django 5.0.6 on 2024-05-28 04:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cyber', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamer',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cyber.game'),
        ),
    ]
