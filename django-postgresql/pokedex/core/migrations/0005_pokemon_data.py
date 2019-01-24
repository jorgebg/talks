import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_pokemon_types'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]
