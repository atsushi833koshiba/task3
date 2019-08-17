import random
import unittest

def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None

    min = ints[0]
    max = ints[0]

    ints = ints[1:]

    for int in ints:
        if min > int:
            min = int
            continue

        if max < int:
            max = int

    return (min, max)

class TestProblem6(unittest.TestCase):

    def test_problem1(self):
        expected = (0, 9)
        l = [i for i in range(0, 10)]  # a list containing 0 - 9
        random.shuffle(l)

        actual = get_min_max(l)
        print('actual: ' + str(actual))
        # Expected:  (0, 9)
        self.assertEqual(expected, actual)

    def test_problem2(self):
        input = [33,2,1,43,2,-4,99122121,3,-45]
        expected = (-45, 99122121)
        actual = get_min_max(input)
        print('actual: ' + str(actual))
        # Expected: (-45, 99122121)
        self.assertEqual(expected, actual)

    def test_problem3(self):
        input = []
        expected = None
        actual = get_min_max(input)
        print('actual: ' + str(actual))
        # Expected: None
        self.assertEqual(expected, actual)


    def test_problem4(self):
        input = [-1]
        expected = (-1, -1)
        actual = get_min_max(input)
        print('actual: ' + str(actual))
        # Expected: (-1, -1)
        self.assertEqual(expected, actual)


    def test_problem5(self):
        input = [i for i in range(-100000, 100000)]  # a list containing 0 - 9
        random.shuffle(input)
        expected = (-100000, 99999)
        actual = get_min_max(input)
        print('actual: ' + str(actual))
        # Expected: (-100000, 99999)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
