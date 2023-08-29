# Generated by Django 4.2.4 on 2023-08-29 20:05

from django.db import migrations, models
import django.db.models.deletion
import dndmusic.base.models.custom_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('music_base', 'load_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Scale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('values', dndmusic.base.models.custom_fields.ListOfStringsField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('scale', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='music_base.scale')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('audio', models.FileField(upload_to='audios/')),
                ('descriptions', models.ManyToManyField(related_name='songs', to='music_base.description')),
            ],
        ),
        migrations.AddField(
            model_name='description',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='descriptions', to='music_base.tag'),
        ),
    ]