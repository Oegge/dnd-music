# Generated by Django 4.2.4 on 2023-09-06 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_base', '0003_alter_song_descriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='duration',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
