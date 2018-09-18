import unittest
from unittest.mock import patch
from magic_ball import MagicBall


class TestInput(unittest.TestCase):

    @patch('builtins.input', side_effect=['yes'])
    def test_replay_input_yes(self, mock):
        self.assertEqual(MagicBall().replay_inputs(), 'yes')

    @patch('builtins.input', side_effect=['no'])
    def test_replay_input_no(self, mock):
        self.assertEqual(MagicBall().replay_inputs(), 'no')

    @patch('builtins.input', side_effect=['No'])
    def test_replay_input_no_uppercase(self, mock):
        self.assertEqual(MagicBall().replay_inputs(), 'no')


    @patch('__main__.MagicBall.replay')
    def test_question_func(self, mock):
        MagicBall().ask_question()
        self.assertTrue(mock.called)


if __name__ == '__main__':
    unittest.main()