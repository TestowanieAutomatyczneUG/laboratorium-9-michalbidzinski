import unittest
from Checker import Checker
from Envi import Envi
from unittest.mock import *
from datetime import datetime
class TestChecker(unittest.TestCase):
    @patch.object(Envi, 'getTime')
    def test_before_17(self, mock_method):
        mock_method.return_value = datetime(2021, 1, 1, 16, 1, 1, 1)
        checker = Checker()
        checker.resetWaw()
        checker.reminder()
        self.assertEqual(False, checker.wav_was_played)

    @patch.object(Envi, 'getTime')
    def test_after_17(self, mock_method):
        mock_method.return_value =  datetime(2021, 1, 1, 23, 1, 1, 1)
        checker = Checker()
        checker.resetWaw()
        checker.reminder()
        self.assertEqual(True, checker.wav_was_played)


