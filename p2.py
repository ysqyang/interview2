#reference: https://blog.csdn.net/jiaomeng/article/details/1495500

import random

_MAX = 1000

class Bloom_filter(object):
    def __init__(self, m, k):
        # m positions, k independent hash functions
        # use simple remainder hashing (x+n)%m
        # use k random values for n to ensure independence
        self.bits = [0]*m  # m positions 
        self.nums = [random.randrange(_MAX) for _ in range(k)] 

    def create_set(self, set_vals):
        for val in set_vals:
            for num in self.nums:
                # use simple remainder hashing
                hash_val = (val+num)%len(self.bits) 
                self.bits[hash_val] = 1

    def is_member(self, val):
        for num in self.nums:
            hash_val = (val+num)%len(self.bits)
            if self.bits[hash_val] == 0:
                return False
        return True

filter = Bloom_filter(10, 5)
print(filter.nums)

vals = [76, 194, 823, 2, 364, 27]

print(vals)

filter.create_set(vals)
print(filter.is_member(2))
print(filter.is_member(823))