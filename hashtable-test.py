import unittest
import random
from hashtable import HashTable

class TestHashTable(unittest.TestCase):

    def testPutAndGet(self):
        ht = HashTable(16)
        ht.put('one', 1)
        ht.put('two', 2)
        ht.put('three',3)
        ht.put('four', 4)
        v = ht.get('three')
        self.assertEqual(v, 3)

    def testBucketStatistics(self):
        ht = HashTable(16)
        for i in range(100):
            key = random.randint(0,1000)
            ht.put(key, i)
        ht.statistics()

if __name__ == '__main__':
    unittest.main()