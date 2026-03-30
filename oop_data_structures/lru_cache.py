# Complexity:
# - Time: get and put are O(1) average and worst-case due to hashmap lookup + linked list operations.
# - Space: O(capacity) for stored cache entries and linked-list nodes.
class ListNode:
    # Node type used by the doubly linked list inside LRUCache.
    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    # LRU cache uses a hash map plus a doubly linked list for O(1) operations.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Maps keys to nodes.
        self.head = ListNode(0, 0)  # Dummy head.
        self.tail = ListNode(0, 0)  # Dummy tail.
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove(self, node: ListNode) -> None:
        # Remove a node from the doubly linked list.
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_front(self, node: ListNode) -> None:
        # Add a node right after the head; it becomes most recently used.
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def _move_to_front(self, node: ListNode) -> None:
        # Move an existing node to the front to mark it as recently used.
        self._remove(node)
        self._add_to_front(node)

    def _pop_tail(self) -> ListNode:
        # Remove the least recently used node from the end.
        node = self.tail.prev
        self._remove(node)
        return node

    def get(self, key: int) -> int:
        # Return the value if present and update its recency.
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_front(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        # Insert or update the key with the given value.
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_front(node)
            return

        node = ListNode(key, value)
        self.cache[key] = node
        self._add_to_front(node)

        if len(self.cache) > self.capacity:
            # Evict the least recently used item when over capacity.
            tail = self._pop_tail()
            del self.cache[tail.key]

# Follow-up: What change would you make to support time-based expiration of cache entries?
# - Store a timestamp for each node and evict entries that exceed a TTL when accessed or during cleanup.
#
# Why doubly-linked list and not singly-linked?
# - A doubly-linked list allows O(1) removal of an arbitrary node when updating recency.
#   Singly-linked lists would require scanning for the previous node.
#
# How would you extend LRU to LFU (Least Frequently Used)?
# - Track access frequency for each key and evict the key with the lowest frequency.
#   A frequency list or heap is typically used, rather than simple recency ordering.
