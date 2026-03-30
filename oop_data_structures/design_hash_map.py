# Fixed-size HashMap approach:
# - Uses a fixed number of buckets and separate chaining for collision handling.
# - The load factor is the number of stored entries divided by the bucket count.
# - This version does not automatically resize, so performance stays simple but can
#   degrade if too many keys are inserted into the fixed bucket array.
# Complexity:
# - Time: put/get/remove average O(1), worst-case O(N) if all keys collide in one bucket.
# - Space: O(N + B) where B is number of buckets; effectively O(N).
class MyHashMap:
    # Simple HashMap implementation using separate chaining for collision handling.
    def __init__(self):
        # Use a prime number of buckets to reduce collisions.
        self._size = 1009
        self._buckets = [[] for _ in range(self._size)]

    def _bucket_index(self, key: int) -> int:
        # Map the key to a bucket index using modulo hashing.
        return key % self._size

    def put(self, key: int, value: int) -> None:
        # Insert or update a key-value pair.
        idx = self._bucket_index(key)
        for i, (k, v) in enumerate(self._buckets[idx]):
            if k == key:
                # If the key already exists, replace its value.
                self._buckets[idx][i] = (key, value)
                return
        # If the key does not exist, append it to the bucket.
        self._buckets[idx].append((key, value))

    def get(self, key: int) -> int:
        # Retrieve the value for the given key, or -1 if not found.
        idx = self._bucket_index(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        # Remove the key from the hash map if it exists.
        idx = self._bucket_index(key)
        for i, (k, v) in enumerate(self._buckets[idx]):
            if k == key:
                self._buckets[idx].pop(i)
                return

# How do you handle Hash collisions in this implementation?
# - We use separate chaining: each bucket stores a list of key-value pairs.
#   Collisions are resolved by appending new items to the same bucket list.
#
# What load factor do you expect for this HashMap, and how would you handle resizing if necessary?
# - With 1009 buckets and N entries, the expected load factor is N / 1009.
#   If the load factor grows too large, resize to a larger bucket array and rehash entries
#   to keep average lookup time close to O(1).
#
# Follow-up: What other collision resolution strategy could you use instead of separate chaining?
# - Open addressing strategies such as linear probing, quadratic probing, or double hashing.

# dynamic resizing would involve:
# Complexity with dynamic resizing:
# - Time: amortized put O(1), get/remove average O(1); worst-case O(N) during resize.
# - Space: O(N + B) where B is the bucket count; effectively O(N).
class MyHashMap:
    def __init__(self, capacity=1009):
        self._size = capacity
        self._buckets = [[] for _ in range(self._size)]
        self._count = 0  # Track the number of key-value pairs.
    
    def _resize(self):
        old_buckets = self._buckets
        self._size *= 2  # Double the number of buckets.
        self._buckets = [[] for _ in range(self._size)]
        self._count = 0  # Reset the count since we're rehashing.
        # Rehash all existing key-value pairs.
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)
    def _bucket_index(self, key: int) -> int:
        return key % self._size
    
    def put(self, key: int, value: int) -> None:
        if self._count / self._size > 0.75:  # Check load factor.
            self._resize()
        idx = self._bucket_index(key)
        for i, (k, v) in enumerate(self._buckets[idx]):
            if k == key:
                self._buckets[idx][i] = (key, value)
                return
        self._buckets[idx].append((key, value))
        self._count += 1

    def get(self, key: int) -> int:
        idx = self._bucket_index(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        idx = self._bucket_index(key)
        for i, (k, v) in enumerate(self._buckets[idx]):
            if k == key:
                self._buckets[idx].pop(i)
                self._count -= 1
                return