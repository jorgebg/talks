from unittest.mock import patch
from django.test import TestCase
from ..models import Round


class IndexTestCase(TestCase):
    fixtures = ['rounds.json']

    def test_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context['rounds'],
            list(Round.objects.order_by('id'))
        )

    @patch('random.choice', return_value='Paper')
    def test_human_vs_ai_play(self, m_random_choice):
        response = self.client.post('/', data={'choice': 'Rock'})
        self.assertEqual(response.status_code, 200)
        game = response.context['rounds'][-1]
        self.assertEqual(game.left, 'Rock')
        self.assertEqual(game.right, 'Paper')
