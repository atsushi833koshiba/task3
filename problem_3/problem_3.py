import unittest

def _swap(from_value, to_value):
    tmp = to_value
    to_value = from_value
    from_value = tmp
    return from_value, to_value


def heapify(list, length, index):

    largest_index = index
    left_index = 2 * index + 1
    right_index = 2 * index + 2

    if left_index < length and  list[largest_index] < list[left_index] :
        largest_index = left_index

    if right_index < length and list[largest_index] < list[right_index]:
        largest_index = right_index

    if largest_index != index:
        list[index], list[largest_index]  = list[largest_index], list[index]
        heapify(list, length , largest_index)


def heap_sort(list):

    list_length = len(list)

    for i in range(list_length, -1, -1):
        heapify(list, list_length, i)

    for i in range(list_length-1, 0, -1):
        list[i], list[0] = list[0], list[i]
        heapify(list, i, 0)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if input_list == None or len(input_list) == 0:
        return None,None

    heap_sort(input_list)

    length = len(input_list) -1

    max1 = ''
    for i in range(length, -1, -2):
        max1 += str(input_list[i])

    max2 = ''
    for i in range(length - 1, -1, -2):
        max2 += str(input_list[i])

    return int(max1), int(max2)



class TestProblem6(unittest.TestCase):

    def test_problem1(self):
        expected = 84,71
        input = [4,1,7,8]
        actual = rearrange_digits(input)
        print('actual: ' + str(actual))
        # Expected: 84, 71
        self.assertEqual(expected, actual)

    def test_problem2(self):
        expected = 531, 42
        input = [1, 2, 3, 4, 5]
        actual = rearrange_digits(input)
        print('actual: ' + str(actual))
        # Expected: 531, 42
        self.assertEqual(expected, actual)

    def test_problem3(self):
        expected = 964,852
        input = [4, 6, 2, 5, 9, 8]
        actual = rearrange_digits(input)
        print('actual: ' + str(actual))
        # Expected: 964, 852
        self.assertEqual(expected, actual)

    def test_problem4(self):
        expected = None,None
        input = []
        actual = rearrange_digits(input)
        print('actual: ' + str(actual))
        # Expected: None
        self.assertEqual(expected, actual)

    def test_problem5(self):
        expected = None,None
        input = None
        actual = rearrange_digits(input)
        print('actual: ' + str(actual))
        # Expected: None
        self.assertEqual(expected, actual)

    def test_problem5(self):
        expected = 0,0
        input = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        actual = rearrange_digits(input)
        print('actual: ' + str(actual))
        # Expected: 0, 0
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
