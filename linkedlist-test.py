import unittest
from linkedlist import LinkedList

class TestLinkedList(unittest.TestCase):

    def testGetStart(self):
        ll = LinkedList()
        ll.insertStart(4)
        ll.insertStart(5)
        v = ll.getStart()
        self.assertEqual(v, 5)

    def testGetEnd(self):
        ll = LinkedList()
        ll.insertStart(4)
        ll.insertEnd(6)
        v = ll.getEnd()
        self.assertEqual(v, 6)

if __name__ == '__main__':
    unittest.main()