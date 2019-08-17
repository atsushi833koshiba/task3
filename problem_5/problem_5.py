import unittest

## Represents a single node in the Trie
class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.children = {}
        self.word_end = False
        self.current_node = None

    def insert(self, char):
        ## Add a child node in this Trie
        self.children[char] = TrieNode()

    def _get_node(self, string):

        node = None
        for char in string:
            if char in self.children:
                node = self.children[char]
        return node

    def _suffixes(self, suffix, node, arr = []):

        if len(suffix) > 1:
            last_char = suffix[-1:]

        if node.word_end:
            arr.append(suffix)

        for child in node.children:
            self._suffixes(suffix + child, node.children[child], arr)

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        result = []

        if suffix == '':
            for child_key in self.children.keys():
                self._suffixes(child_key, self.children[child_key], result)

        return result

## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()

    def insert(self, word):
        ## Add a word to the Trie

        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.insert(char)
            current_node = current_node.children[char]
        current_node.word_end = True


    def find(self, prefix):
        ## Find the Trie node that represents this prefix

        current_node = self.root

        for char in prefix:
            if char in current_node.children:
                current_node = current_node.children[char]
            else:
                return None

        return current_node


class TestProblem5(unittest.TestCase):

    def test_problem1(self):
        expected = ["h","hmaster","hnology"]
        t = Trie()
        t.insert("tech")
        t.insert("techmaster")
        t.insert("technology")
        t.insert("ted")
        nd = t.find("tec")

        actual = nd.suffixes()
        print('actual: ' + str(actual))
        # Expected: ['h', 'hmaster', 'hnology']
        self.assertEqual(expected, actual)


    def test_problem2(self):
        expected = ["hology","agonist","onym"]
        MyTrie = Trie()
        wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
        ]
        for word in wordList:
            MyTrie.insert(word)

        nd = MyTrie.find("ant")
        actual = nd.suffixes()
        print('actual: ' + str(actual))
        # Expected: ["hology","agonist","onym"]
        self.assertEqual(expected, actual)


    def test_problem3(self):
        expected = None
        MyTrie = Trie()
        wordList = []
        for word in wordList:
            MyTrie.insert(word)

        actual = MyTrie.find("nothing")

        print('actual: ' + str(actual))
        # Expected: None
        self.assertEqual(expected, actual)


    def test_problem4(self):
        expected = None
        MyTrie = Trie()
        wordList = [
        "ant", "anthology", "antagonist", "antonym",
        "fun", "function", "factory",
        "trie", "trigger", "trigonometry", "tripod"
        ]
        for word in wordList:
            MyTrie.insert(word)

        actual = MyTrie.find("s")
        print('actual: ' + str(actual))
        # Expected: None
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
