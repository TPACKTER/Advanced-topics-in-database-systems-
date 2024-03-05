import math
import mmh3

class BloomFilter:
    def __init__(self, n, p):
        self.m = int(-(n * math.log(p)) / (math.log(2) ** 2))  # optimal size of bloom filter
        self.k = int((self.m / n) * math.log(2))  # number of hash functions
        self.bit_array = [False] * self.m

    def add(self, item):
        for i in range(self.k):
            index = mmh3.hash(item, i) % self.m
            self.bit_array[index] = True

    def __contains__(self, item):
        for i in range(self.k):
            index = mmh3.hash(item, i) % self.m
            if not self.bit_array[index]:
                return False
        return True

def bloom_join(list1, list2):
    # bloom join is a faster unsafe version of semi join
    # it creates a bit vector to each data-set, send it back and forth and filter the commen data
    bloom_filter = BloomFilter(len(list1), 0.05)  # Adjust the false positive rate as needed
    for item in list1:
        bloom_filter.add(item)

    common_elements = []
    for item in list2:
        if item in bloom_filter:
            common_elements.append(item)

    return common_elements

# Example usage:
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(bloom_join(list1, list2))  # Output: [4, 5]
