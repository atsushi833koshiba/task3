import unittest

def _find_rotation_recursion(lower, upper, list):

    mid = (lower + upper) // 2

    if lower >= upper:
        return -1

    next = mid + 1
    if next < upper:
        if list[next] < list[mid]:
            return next

    previous = mid - 1
    if previous >= lower:
        if list[previous] > list[mid]:
            return mid

    # Search right side.
    if list[mid] > list[upper]:
        return _find_rotation_recursion(mid, upper, list)

    else:
        return _find_rotation_recursion(lower, mid, list)


def find_rotation(list):
    return _find_rotation_recursion(0, len(list)-1, list)



def _binary_search(lower, upper, target, list):

    if upper < lower:
        return -1
    mid = (lower + upper) // 2

    if list[mid] == target:
        return mid

    if list[mid] > target:
        return _binary_search(lower, mid - 1 , target, list)
    else:
        return _binary_search(mid + 1, upper, target, list)



def find_number(pivot, target_number, input_list):

    previous = pivot - 1
    next = pivot + 1

    left_result = _binary_search(0, previous, target_number, input_list)
#    print("left: " + str(left_result))

    if not left_result == -1:
        return left_result

    right_result = _binary_search(next, len(input_list)-1, target_number, input_list)
#    print("right: " + str(right_result))

    if not right_result == -1:
        return right_result

    return -1


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    pivot = find_rotation(input_list)
    print('pivot: ' + str(pivot))

    result = find_number(pivot, number, input_list)
    print("result: " + str(result))



def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

# input = [6, 7, 8, 9, 10, 1, 2, 3, 4]
# rotated_array_search(input, 6)
# input = [4,5,6, 7, 8, 9, 10, 0, 1, 2, 3]
# rotated_array_search(input, 6)


class TestProblem2(unittest.TestCase):

    def test_problem1(self):
        input = [6, 7, 8, 9, 10, 1, 2, 3, 4]
        expected = linear_search(input, 6)
        actual = linear_search(input, 6)

        print('actual: ' + str(actual))
        # Expected: 0

        self.assertEqual(expected, actual)


    def test_problem2(self):
        input = [4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3]
        expected = linear_search(input, 10)
        actual = linear_search(input, 10)

        print('actual: ' + str(actual))
        # Expected: 6

        self.assertEqual(expected, actual)


    def test_problem3(self):
        input = []
        expected = linear_search(input, 255)
        actual = linear_search(input, 255)

        print('actual: ' + str(actual))
        # Expected: -1

        self.assertEqual(expected, actual)


    def test_problem4(self):
        input = [9, 12, 66, 45 , 268, 9992, 10682, 0 , 1 ,2, 3 ,7]
        expected = linear_search(input, 268)
        actual = linear_search(input, 268)
        print('actual: ' + str(actual))
        # Expected: 4
        self.assertEqual(expected, actual)


    def test_problem5(self):
        input = [0,1,2,3,4,5]
        expected = linear_search(input, 1)
        actual = linear_search(input, 1)
        print('actual: ' + str(actual))
        # Expected: 1
        self.assertEqual(expected, actual)


    def test_problem6(self):
        input = [0,1,2,3,4,5]
        expected = linear_search(input, 1)
        actual = linear_search(input, 1)
        print('actual: ' + str(actual))
        # Expected: -1
        self.assertEqual(expected, actual)


    def test_problem7(self):
        input = [0,1,2,3,4,5]
        expected = linear_search(input, 11111111111111111111111111111111111111111111111111111111111)
        actual = linear_search(input, 11111111111111111111111111111111111111111111111111111111111)
        print('actual: ' + str(actual))
        # Expected: -1
        self.assertEqual(expected, actual)



if __name__ == '__main__':
    unittest.main()
