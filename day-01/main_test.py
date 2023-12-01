import unittest
from main import *

class TestCalibration(unittest.TestCase):
    def test_get_first_digit(self):
        self.assertEqual(get_first_digit("aaaa1aa3aa5aaa"), '1')
        self.assertEqual(get_first_digit("2aaa1aa3aa5aaa"), '2')
        self.assertEqual(get_first_digit("aaaaaaaaaaaaa3"), '3')
        self.assertEqual(get_first_digit("4aaaaaaaaaaaaa"), '4')

    def test_get_last_digit(self):
        self.assertEqual(get_last_digit("aaaa1aa3aa5aaa"), '5')
        self.assertEqual(get_last_digit("aaaa1aa3aa5aa2"), '2')
        self.assertEqual(get_last_digit("aaaaaaaaaaaaa3"), '3')
        self.assertEqual(get_last_digit("4aaaaaaaaaaaaa"), '4')

    def test_calibration_value(self):
        self.assertEqual(calibration_value("aaaa1aa3aa5aaa"), 15)
        self.assertEqual(calibration_value("2aaa1aa3aa5aa2"), 22)

    def test_calibration(self):
        self.assertEqual(calibrate('test_input.txt'), 142)


if __name__ == '__main__':
    unittest.main()