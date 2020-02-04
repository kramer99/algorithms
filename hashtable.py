import numpy as np
from linkedmap import LinkedMap

"""
A simple hash table. You can choose the number of buckets at initialization, but
it does not dynamically resize. Needs a delete op too. There's no reason for anyone
to actually use this though, as the built-in dictionary construct in Python does the 
same thing, but better.
"""
class HashTable:

    def __init__(self, bucketCount = 256):
        self.n = 0
        self.bucketCount = bucketCount
        self.buckets = [None] * bucketCount     # Python can't do normal arrays of objects like Java, so this weirdeness

    def put(self, key, value):
        # Python's built-in hashing functions for simple types will generate
        # values in the full int range, so we modulus it by the bucket count
        h = hash(key) % self.bucketCount
        if self.buckets[h] == None:
            # leverage our earlier linked map implementation
            map = LinkedMap()
            map.insertStart(key, value)
            self.buckets[h] = map
        else:
            self.buckets[h].insertEnd(key, value)
        self.n = self.n + 1

    def get(self, key):
        h = hash(key) % self.bucketCount
        return self.buckets[h].get(key)

    def statistics(self):
        sizes = []
        for i, bucket in enumerate(self.buckets):
            size = bucket.size if bucket != None else 0
            print('bucket', i, ':', size)
            sizes.append(size)        
        print('mean bucket size: ', np.mean(np.array(sizes)))        
        print('std deviation   : ', np.std(np.array(sizes)))