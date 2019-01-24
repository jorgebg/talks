import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_pokemon_search_vector'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='types',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=10), default=list, size=None),
        ),
    ]
