import unittest
from main import *

class TestCalibration(unittest.TestCase):
    def test_get_first_digit(self):
        self.assertEqual(get_first_digit("aaaa1aa3aa5aaa"), '1')
        self.assertEqual(get_first_digit("2aaa1aa3aa5aaa"), '2')
        self.assertEqual(get_first_digit("aaaaaaaaaaaaa3"), '3')
        self.assertEqual(get_first_digit("4aaaaaaaaaaaaa"), '4')
        self.assertEqual(get_first_digit("two1nine"), '2')
        self.assertEqual(get_first_digit("eightwothree"), '8')
        self.assertEqual(get_first_digit("abcone2threexyz"), '1')
        self.assertEqual(get_first_digit("7pqrstsixteen"), '7')

    def test_get_last_digit(self):
        self.assertEqual(get_last_digit("aaaa1aa3aa5aaa"), '5')
        self.assertEqual(get_last_digit("aaaa1aa3aa5aa2"), '2')
        self.assertEqual(get_last_digit("aaaaaaaaaaaaa3"), '3')
        self.assertEqual(get_last_digit("4aaaaaaaaaaaaa"), '4')
        self.assertEqual(get_last_digit("two1nine"), '9')
        self.assertEqual(get_last_digit("eightwothree"), '3')
        self.assertEqual(get_last_digit("abcone2threexyz"), '3')
        self.assertEqual(get_last_digit("7pqrstsixteen"), '6')

    def test_calibration_value(self):
        self.assertEqual(calibration_value("aaaa1aa3aa5aaa"), 15)
        self.assertEqual(calibration_value("2aaa1aa3aa5aa2"), 22)
        self.assertEqual(calibration_value("two1nine"), 29)
        self.assertEqual(calibration_value("eightwothree"), 83)
        self.assertEqual(calibration_value("abcone2threexyz"), 13)
        self.assertEqual(calibration_value("7pqrstsixteen"), 76)

    def test_calibration(self):
        self.assertEqual(calibrate('test_input.txt'), 142)
        self.assertEqual(calibrate('test_input_with_words.txt'), 281)




if __name__ == '__main__':
    unittest.main()