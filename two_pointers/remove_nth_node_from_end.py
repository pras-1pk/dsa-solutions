"""Remove Nth Node From End of List.
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """Remove the nth node from the end of the list and return the head."""
    # Brute force approach:
    # - First traverse the list to compute its length L.
    # - Then traverse again to the (L-n)th node and remove the next node.
    # - Time: O(L) for the first pass + O(L) for the second pass = O(L).
    # - Space: O(1).
    # Optimized two-pointer approach:
    # - Use a fast pointer advanced n steps ahead of slow.
    # - Then move both pointers until fast reaches the end.
    # - Slow ends up just before the node to remove.
    # - Time: O(L), Space: O(1).
    # Complexity:
    # - Time: O(L), where L is the length of the list.
    # - Space: O(1).
    # Generalization to "find the kth node from the end":
    # - Use the same n-step gap between fast and slow.
    # - Advance fast by k, then move both pointers together until fast reaches the list end.
    # - At that point, slow points to the kth node from the end (or just before it depending
    #   on whether you start slow from head or from a dummy node).
    dummy = ListNode(0, head)
    slow, fast = dummy, dummy
    for _ in range(n):
        fast = fast.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return dummy.next
    