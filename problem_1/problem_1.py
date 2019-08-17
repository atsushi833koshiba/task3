import unittest

def _sqrt(lower, target, upper, accuracy_weight):

    mid = float((lower + upper) / 2)
    squre_mid = mid ** 2

    # End condtion 1
    if target == squre_mid:
        return mid

    if squre_mid > target:
        upper = mid
    elif squre_mid < target:
        lower = mid

    # End condtion 2
    # The deference is within the margin of error according to the given accuracy_weight.
    if upper - lower < accuracy_weight:
        return mid

    return _sqrt(lower, target, upper, accuracy_weight)


def sqrt(number):
    return int(_sqrt(0, number, number, 1e-10))


class TestProblem1(unittest.TestCase):

    def test_problem1(self):
        input = 2
        expected = 1
        actual = sqrt(input)
        print('actual: ' + str(actual))
        # Expected: 1
        self.assertEqual(expected, actual)

    def test_problem2(self):
        input = 16
        expected = 4
        actual = sqrt(input)
        print('actual: ' + str(actual))
        # Expected: 4
        self.assertEqual(expected, actual)

    def test_problem3(self):
        input = 27
        expected = 5
        actual = sqrt(input)
        print('actual: ' + str(actual))
        # Expected: 5
        self.assertEqual(expected, actual)


    def test_problem4(self):
        input = 0
        expected = 0
        actual = sqrt(input)
        print('actual: ' + str(actual))
        # Expected: 0
        self.assertEqual(expected, actual)

    def test_problem5(self):
        input = 99999
        expected = 316
        actual = sqrt(input)
        print('actual: ' + str(actual))
        # Expected: 33333354137
        self.assertEqual(expected, actual)

    def test_problem6(self):
        input = 123456789
        expected = 11111
        actual = sqrt(input)
        print('actual: ' + str(actual))
        # Expected: 33333354137
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
