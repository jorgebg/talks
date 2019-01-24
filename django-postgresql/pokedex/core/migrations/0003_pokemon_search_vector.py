import django.contrib.postgres.search
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_fts_extensions'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='search_vector',
            field=django.contrib.postgres.search.SearchVectorField(null=True, default=None),
            preserve_default=False,
        ),
    ]
