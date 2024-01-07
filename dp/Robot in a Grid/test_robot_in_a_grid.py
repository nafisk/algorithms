import unittest
from robot_in_a_grid import find_path

class TestRobotInAGrid(unittest.TestCase):

    def test_valid_path(self):
        grid = [
            [0, 1, 0, 0],
            [0, 0, 0, 1],
            [1, 0, 0, 0],
            [0, 0, 1, 0]
        ]
        expected_path = [(0, 0), (0, 1), (1, 1), (1, 2), (1, 3), (2, 3), (3, 3)]
        self.assertEqual(find_path(grid), expected_path)

    def test_no_path(self):
        grid = [
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.assertIsNone(find_path(grid))

    def test_empty_grid(self):
        grid = []
        self.assertIsNone(find_path(grid))

    def test_small_grid(self):
        grid = [[0]]
        expected_path = [(0, 0)]
        self.assertEqual(find_path(grid), expected_path)

    def test_large_grid(self):
        grid = [[0] * 100] * 100
        expected_path = [(0, 0)] + [(0, i) for i in range(1, 100)] + [(i, 99) for i in range(1, 100)]
        self.assertEqual(find_path(grid), expected_path)

if __name__ == '__main__':
    print('_________STARTING TEST__________')
    unittest.main()
