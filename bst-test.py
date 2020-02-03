import unittest
from bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def testGetEntry(self):
        bst = BinarySearchTree()
        bst.insert('g', 4)
        bst.insert('x', 2)
        bst.insert('y', 7)
        bst.insert('a', 6)
        v = bst.get('y')
        self.assertEqual(v, 7)

    def testGetInvalidEntry(self):
        bst = BinarySearchTree()
        bst.insert('g', 4)
        bst.insert('x', 2)
        bst.insert('y', 7)
        bst.insert('a', 6)
        v = bst.get('m')
        self.assertIsNone(v)

if __name__ == '__main__':
    unittest.main()