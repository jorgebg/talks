from django.test import TestCase
from ..models import BEATS, Outcome, Round


class BeatsTestCase(TestCase):
    def test_rock_beats_scissors(self):
        self.assertEqual(BEATS.get('Rock'), 'Scissors')

    def test_paper_beats_rock(self):
        self.assertEqual(BEATS.get('Paper'), 'Rock')

    def test_scissors_beats_paper(self):
        self.assertEqual(BEATS.get('Scissors'), 'Paper')

    def test_unknown(self):
        self.assertIsNone(BEATS.get('Spock'))


class RoundTestCase(TestCase):
    def test_left_wins(self):
        round = Round(left='Paper', right='Rock')
        self.assertEqual(round.outcome, Outcome.left)

    def test_right_wins(self):
        round = Round(left='Rock', right='Paper')
        self.assertEqual(round.outcome, Outcome.right)

    def test_draw(self):
        round = Round(left='Scissors', right='Scissors')
        self.assertEqual(round.outcome, Outcome.draw)


class ViewClientTestCase(TestCase):

    def setUp(self):
        Round.objects.create(left='Paper', right='Rock')
        Round.objects.create(left='Rock', right='Paper')

    def test_content(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode()
        self.assertInHTML('<p>Choose a shape</p>', content)
        self.assertInHTML('<li>Paper vs Rock: left</li>', content)
        self.assertInHTML('<li>Rock vs Paper: right</li>', content)


class ViewFixturesTestCase(TestCase):
    fixtures = ['rounds.json']

    def test_content(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        content = response.content.decode()
        self.assertInHTML('<p>Choose a shape</p>', content)
        self.assertInHTML('<li>Paper vs Rock: left</li>', content)
        self.assertInHTML('<li>Rock vs Paper: right</li>', content)
