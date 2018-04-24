from enum import Enum
from django.db import models


SHAPES = ('Rock', 'Paper', 'Scissors')

BEATS = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper',
}


class Outcome(Enum):
    draw = 0
    left = 1
    right = 2


class Round(models.Model):
    left = models.CharField(max_length=10)
    right = models.CharField(max_length=10)

    @property
    def outcome(self):
        if self.left == self.right:
            return Outcome.draw
        if BEATS.get(self.left) == self.right:
            return Outcome.left
        if BEATS.get(self.right) == self.left:
            return Outcome.right

    def __str__(self):
        return '{} vs {}: {}'.format(
            self.left, self.right, self.outcome.name
        )
