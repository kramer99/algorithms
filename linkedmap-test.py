import unittest
from linkedmap import LinkedMap

class TestLinkedMap(unittest.TestCase):

    def testInsertStart(self):
        lm = LinkedMap()
        lm.insertStart('four', 4)
        v = lm.getStart()
        self.assertEqual(v, 4)

    def testInsertEnd(self):
        lm = LinkedMap()
        lm.insertEnd('four', 4)
        v = lm.getEnd()
        self.assertEqual(v, 4)
        lm.insertEnd('five', 5)
        v = lm.getEnd()
        self.assertEqual(v, 5)

    def testGet(self):
        lm = LinkedMap()
        lm.insertStart('five', 5)
        lm.insertStart('four', 4)
        lm.insertStart('three', 3)
        v = lm.get('four')
        self.assertEqual(v, 4)

if __name__ == '__main__':
    unittest.main()