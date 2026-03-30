# Complexity:
# - Time: add/remove/contains average O(1), worst-case O(N) if a bucket contains many keys.
# - Space: O(N + B) where B is number of buckets; effectively O(N).
class MyHashSet:
    # Simple HashSet implementation using bucket lists for collision handling.
    def __init__(self):
        # Choose a prime number of buckets to improve distribution.
        self._size = 1009
        self._buckets = [[] for _ in range(self._size)]

    def _hash(self, key: int) -> int:
        # Calculate the bucket index for the key.
        return key % self._size

    def add(self, key: int) -> None:
        # Add the key only if it is not already present.
        idx = self._hash(key)
        if key not in self._buckets[idx]:
            self._buckets[idx].append(key)

    def remove(self, key: int) -> None:
        # Remove the key if it exists; ignore otherwise.
        idx = self._hash(key)
        try:
            self._buckets[idx].remove(key)
        except ValueError:
            pass

    def contains(self, key: int) -> bool:
        # Check membership by scanning the bucket.
        idx = self._hash(key)
        return key in self._buckets[idx]

# Follow-up: How would you modify this structure to support dynamic resizing?
# - Track the number of stored elements and the current bucket count.
#   When the load factor exceeds a threshold (for example 0.75), create a larger
#   bucket array and rehash every key into the new buckets.
