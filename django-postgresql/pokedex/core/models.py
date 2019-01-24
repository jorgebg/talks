from django.contrib.postgres.fields import ArrayField, JSONField
from django.contrib.postgres.search import SearchVectorField
from django.db import models


class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    search_vector = SearchVectorField(null=True)
    types = ArrayField(models.CharField(max_length=10), default=list)
    data = JSONField(default=dict)

    def __str__(self):
        return self.name


from django.contrib.postgres.fields import DateTimeRangeField


class Battle(models.Model):
    a = models.ForeignKey(Pokemon, related_name='+', on_delete=models.CASCADE)
    b = models.ForeignKey(Pokemon, related_name='+', on_delete=models.CASCADE)
    schedule = DateTimeRangeField()

    def __str__(self):
        return f'{self.a} vs {self.b}'
