import unittest

# Exception class for url.
class IllegalURLException(Exception):
    pass

# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler='Root handler'):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode('/', handler)

    def insert(self, path, registerd_handler, default_handler, current_node=None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path

        # Recursive End Condition
        if path == '' or path == None:
            return

        try:
            if len(path) > 1 and '//' in path:
                    raise ValueError
        except ValueError:
            print('Error: You input illegal url, Please check it. URL is {} .'.format(path))
            raise IllegalURLException

        if path[len(path)-1] == '/':
            path = path[0:len(path)-1]

        path_arr = path.split('/')
        currrent_path = path_arr[0]
        current_handler = None

        # Deepest path case
        if len(path_arr) == 1:
            current_handler = registerd_handler
        else:
            current_handler = default_handler

        if current_node != None:
            if currrent_path not in current_node.children:
                current_node.children[currrent_path] = RouteTrieNode(currrent_path, current_handler)

            if len(path_arr) > 1:
                path_arr = path_arr[1:]
                path_string = '/'.join(path_arr)
            else:
                # Set blank to finish recursive.
                path_string = ''

            self.insert(path_string, registerd_handler, default_handler, current_node.children[currrent_path])

        else:
            # first case
            if len(path_arr) > 1 and path_arr[0] == '':
                path_arr = path_arr[1:]

            path_string = '/'.join(path_arr)
            self.insert(path_string, registerd_handler, default_handler, self.root)


    def find(self, path, default=None):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if path == '' or path == None:
            return None

        if path[len(path)-1] == '/':
            path = path[0:len(path)-1]

        if self.root.path == path:
            return self.root.handler

        path_arr = path.split('/')
        path_arr = path_arr[1:]
        current_node = self.root

        for path in path_arr:
            if path in current_node.children:
                current_node = current_node.children[path]
            else:
                current_node = None
                break

        if current_node != None:
            return current_node.handler
        return default

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, path, handler=None):
        # Initialize the node with children as before, plus a handler
        self.path = path
        self.handler = handler
        self.children = {}

    def insert(self, path, handler=None):
        # Insert the node as before
        self.children[path] = handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler, default_handler):
        self.router_trie = RouteTrie(root_handler)
        self.default_handler = default_handler

    def add_handler(self, path, handler):
        self.router_trie.insert(path, handler, self.default_handler)

    def lookup(self, path):
        return  self.router_trie.find(path, self.default_handler)


class TestProblem7(unittest.TestCase):

    def test_problem1(self):
        router = Router("Root handler", 'Not found handler')

        expected = "Root handler"
        actual = router.lookup('/')

        print('actual: ' + actual)
        # Expected: Root handler
        self.assertEqual(expected, actual)


    def test_problem2(self):
        router = Router("Root handler", 'Not found handler')

        expected = "Apache Handler"

        router.add_handler("/home/apache", "Apache Handler")
        actual = router.lookup('/home/apache')

        print('actual: ' + actual)
        # Expected: Apache Handler
        self.assertEqual(expected, actual)


    def test_problem3(self):
        router = Router("Root handler", 'Not found handler')

        expected = "Apache HTTP Handler"

        router.add_handler("/home/apache/http", "Apache HTTP Handler")
        actual = router.lookup('/home/apache/http/')

        print('actual: ' + actual)
        # Expected: Apache HTTP Handler
        self.assertEqual(expected, actual)


    def test_problem4(self):
        router = Router("Root handler", 'Not found handler')

        expected = "Not found handler"

        router.add_handler("/home/apache", "Apache Handler")
        actual = router.lookup('/home/apache/nothing')

        print('actual: ' + actual)
        # Expected: Not found handler
        self.assertEqual(expected, actual)


    def test_problem5(self):
        router = Router("Root handler", 'Not found handler')

        with self.assertRaises(IllegalURLException):
            router.add_handler("/home/ill////////////", "Ill Handler")
            # Expected : Error: You input illegal url, Please check it. URL is /home/ill//////////// .


    def test_problem6(self):
        router = Router("Root handler", 'Not found handler')

        with self.assertRaises(IllegalURLException):
            router.add_handler("/home/ill//second", "Ill Handler")
            # Expected : Error: You input illegal url, Please check it. URL is /home/ill//second .


    def test_problem7(self):
        router = Router("Root handler", 'Not found handler')

        expected = "G Handler"

        router.add_handler("/home/apache", "Apache Handler")
        router.add_handler("/home/apache/a", "A Handler")
        router.add_handler("/home/apache/b", "B Handler")
        router.add_handler("/home/apache/c", "C Handler")
        router.add_handler("/home/apache/d/", "D Handler")
        router.add_handler("/home/apache/e/", "E Handler")
        router.add_handler("/home/apache/f", "F Handler")
        router.add_handler("/home/apache/g/", "G Handler")
        actual = router.lookup('/home/apache/g')

        print('actual: ' + actual)
        # Expected: G Handler
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
