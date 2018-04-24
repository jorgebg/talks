from django.test import SimpleTestCase
from ..models import BEATS, Outcome, Round


class BeatsTestCase(SimpleTestCase):
    def test_rock_beats_scissors(self):
        self.assertEqual(BEATS.get('Rock'), 'Scissors')

    def test_paper_beats_rock(self):
        self.assertEqual(BEATS.get('Paper'), 'Rock')

    def test_scissors_beats_paper(self):
        self.assertEqual(BEATS.get('Scissors'), 'Paper')

    def test_unknown(self):
        self.assertIsNone(BEATS.get('Spock'))


class RoundTestCase(SimpleTestCase):
    def test_left_wins(self):
        round = Round(left='Paper', right='Rock')
        self.assertEqual(round.outcome, Outcome.left)

    def test_right_wins(self):
        round = Round(left='Rock', right='Paper')
        self.assertEqual(round.outcome, Outcome.right)

    def test_draw(self):
        round = Round(left='Scissors', right='Scissors')
        self.assertEqual(round.outcome, Outcome.draw)
