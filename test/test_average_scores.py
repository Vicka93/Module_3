"""
Author:Viktoriia Denys
Program:average_scores.py
program average_scores.py reads in one person's names, first and last, their age and three scores out of 100.
Taking the three scores and finding the average, storing into a variable.
"""


import unittest
from unittest import mock

from format_output import average_scores as topic2


class MyTestCase(unittest.TestCase):
    def test_average(self):
        with mock.patch('builtins.input', side_effect=[85, 90, 95]):
            assert topic2.average() == 90


if __name__ == '__main__':
    unittest.main()
