from django.core.management import call_command
from django.db import migrations

def load_fixture(apps, schema_editor):
    call_command('loaddata', 'user')

def unload_fixture(apps, schema_editor):
    call_command('flush')

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.RunPython(load_fixture, unload_fixture),
    ]