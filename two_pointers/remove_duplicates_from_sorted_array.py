"""Remove Duplicates from Sorted Array.

Placeholder file. Implementation not provided yet.
"""

from typing import List


def remove_duplicates_from_sorted_array(nums: List[int]) -> int:
    """Remove duplicates in-place and return the new length."""
    # Brute force approach:
    # - Scan the array and remove duplicates by shifting later elements left.
    # - Each duplicate removal may require shifting O(n) elements.
    # - Time: O(n^2) worst-case, Space: O(1).
    # Optimized two-pointer approach:
    # - Maintain `k` as the last index of the deduplicated prefix.
    # - Use `i` to scan ahead and copy a new value only when it differs from nums[k].
    # - Time: O(n), Space: O(1).
    # This is optimal for a sorted array because it processes each element once.
    # Extension to allow at most `allowed` duplicates:
    # - With `allowed = k_allowed`, compare nums[i] to nums[k - allowed + 1]
    #   instead of nums[k].
    # - Minimal change: use
    #     if k < allowed - 1 or nums[i] != nums[k - allowed + 1]:
    #   then advance the write position and copy nums[i].
    # Why this is called a "slow-fast pointer" pattern:
    # - `k` lags behind as the write/slow pointer, while `i` moves ahead as the fast pointer.
    # - The technique relies on the relative distance between them, not just having two pointers.
    k = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[k]:
            k += 1
            nums[k] = nums[i]
    return k + 1

# Follow-up: How would you modify the algorithm to allow at most `k` duplicates instead of just one?
    if not nums:
        return 0
    if len(nums) <= k:
        return len(nums)    
    i = k
    for j in range(k, len(nums)):
        if nums[j] != nums[i - k]:
            nums[i] = nums[j]
            i += 1
    return i
