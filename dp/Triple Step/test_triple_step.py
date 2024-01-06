# test_triple_step.py
import unittest
from triple_step import tripleStepBottomUp as count_ways_to_climb_stairs

class TestTripleStep(unittest.TestCase):

    def print_result(self, test_name, result, actual, expected):
        if result:
            print(f"✅ Passed {test_name} - Actual: {actual}, Expected: {expected}")
        else:
            print(f"❌ Failed {test_name} - Actual: {actual}, Expected: {expected}")

    def test_count_ways_with_negative_steps(self):
        result = count_ways_to_climb_stairs(-1)
        self.print_result("test_count_ways_with_negative_steps", result == 0, result, 0)
        self.assertEqual(result, 0)

    def test_count_ways_with_zero_steps(self):
        result = count_ways_to_climb_stairs(0)
        self.print_result("test_count_ways_with_zero_steps", result == 1, result, 1)
        self.assertEqual(result, 1)

    def test_count_ways_with_one_step(self):
        result = count_ways_to_climb_stairs(1)
        self.print_result("test_count_ways_with_one_step", result == 1, result, 1)
        self.assertEqual(result, 1)

    def test_count_ways_with_two_steps(self):
        result = count_ways_to_climb_stairs(2)
        self.print_result("test_count_ways_with_two_steps", result == 2, result, 2)
        self.assertEqual(result, 2)

    def test_count_ways_with_three_steps(self):
        result = count_ways_to_climb_stairs(3)
        self.print_result("test_count_ways_with_three_steps", result == 4, result, 4)
        self.assertEqual(result, 4)

    def test_count_ways_with_large_number_of_steps(self):
        result = count_ways_to_climb_stairs(10)
        self.print_result("test_count_ways_with_large_number_of_steps", result == 274, result, 274)
        self.assertEqual(result, 274)

if __name__ == '__main__':
    unittest.main(verbosity=0)
