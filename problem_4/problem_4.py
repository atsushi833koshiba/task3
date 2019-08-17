import unittest

def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    if input_list == None or len(input_list) == 0:
        return None

    list_0 = []
    list_others = []

    for input in input_list:

        if input == 0:
            list_0.append(input)
        elif input == 2:
            list_others.append(input)
        else:
            list_others.insert(0, input)

    list_0.extend(list_others)

    return list_0


class TestProblem3(unittest.TestCase):


    def test_problem1(self):
        input = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
        expected = sorted(input)
        actual = sort_012(input)
        print('actual: ' + str(actual))
        # Expected: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
        self.assertEqual(expected, actual)

    def test_problem2(self):
        input = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
        expected = sorted(input)
        actual = sort_012(input)
        print('actual: ' + str(actual))
        # Expected: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        self.assertEqual(expected, actual)

    def test_problem3(self):
        input = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        expected = sorted(input)
        actual = sort_012(input)
        print('actual: ' + str(actual))
        # Expected: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
        self.assertEqual(expected, actual)

    def test_problem3(self):
        input = None
        expected = None
        actual = sort_012(input)
        print('actual: ' + str(actual))
        # Expected: None
        self.assertEqual(expected, actual)

    def test_problem4(self):
        input = []
        expected = None
        actual = sort_012(input)
        print('actual: ' + str(actual))
        # Expected: None
        self.assertEqual(expected, actual)


    def test_problem5(self):
        input = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,2,2,2,2,1,1,1,1,1,1,0
        ,1,2,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,1]
        expected = sorted(input)
        actual = sort_012(input)
        print('actual: ' + str(actual))
        # Expected:  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
        # 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2,
        # 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
