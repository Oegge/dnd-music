# Generated by Django 4.2.4 on 2024-05-20 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_base', '0004_alter_song_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='last_played',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
