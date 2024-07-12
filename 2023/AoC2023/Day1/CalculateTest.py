import unittest
from Day1.part2 import calculate
from parameterized.parameterized import parameterized


class TestCalculator(unittest.TestCase):
    @parameterized.expand([
        (['eightwothree'], 83),
        (['9vxfg'], 99),
        (['two1nine'], 29),
        (['eightwothree'], 83),
        (['abcone2threexyz'], 13),
        (['xtwone3four'], 24),
        (['4nineeightseven2'], 42),
        (['zoneight234'], 14),
        (['7pqrstsixteen'], 76)
    ])
    def test_calculate(self, input, expected_output):
        result = calculate(input)
        self.assertEqual(expected_output, result)
