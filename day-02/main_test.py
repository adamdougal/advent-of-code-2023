import unittest
from main import *

class Test(unittest.TestCase):
    
    def test_parse(self):
        filePath = 'test_input.txt'
        games = parse_input(filePath)
        self.assertIn([{'red': 4, 'blue': 3}, {'red': 1, 'blue': 6, 'green': 2}, {'green': 2}], games)
        self.assertIn([{'blue': 1, 'green': 2}, {'green': 3, 'blue': 4, 'red': 1}, {'green': 1, 'blue': 1}], games)
        self.assertIn([{'green': 8, 'blue': 6, 'red': 20}, {'blue': 5, 'red': 4, 'green': 13}, {'green': 5, 'red': 1}], games)
        self.assertIn([{'green': 1, 'red': 3, 'blue': 6}, {'green': 3, 'red': 6}, {'green': 3, 'blue': 15, 'red': 14}], games)
        self.assertIn([{'red': 6, 'blue': 1, 'green': 3}, {'blue': 2, 'red': 1, 'green': 2}], games)
        
        
    def test_game_possible(self):
        game = [{'red': 4, 'blue': 3}, {'red': 1, 'blue': 6, 'green': 2}, {'green': 2}]
        self.assertTrue(game_possible(game, {'red': 10, 'blue': 10, 'green': 10}))
        self.assertFalse(game_possible(game, {'red': 1, 'blue': 1, 'green': 1}))
        self.assertFalse(game_possible(game, {'red': 0, 'blue': 0, 'green': 0}))
        
        
    def test_number_of_games_possible(self):
        filePath = 'test_input.txt'
        self.assertEqual(id_sum_of_games_possible(filePath, {'red': 12, 'blue': 14, 'green': 13}), 8)
        
        
    def test_power(self):
        self.assertEqual(power({'red': 2, 'blue': 3, 'green': 1}), 6)
        self.assertEqual(power({'red': 2, 'blue': 3, 'green': 5}), 30)
        self.assertEqual(power({'red': 2, 'blue': 3, 'green': 0}), 0)
        
    
    def test_minimum_required_for_game(self):
        self.assertEqual(minimum_required_for_game(
            [{'red': 4, 'blue': 3}, {'red': 1, 'blue': 6, 'green': 2}, {'green': 2}]), 
            {'red': 4, 'blue': 6, 'green': 2})

    
    def test_sum_of_minimum_powers(self):
        filePath = 'test_input.txt'
        self.assertEqual(sum_of_minimum_powers(filePath), 2286)
        
if __name__ == '__main__':
    unittest.main()