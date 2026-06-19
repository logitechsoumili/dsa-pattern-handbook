# Remove Duplicates from Sorted Array

## Problem Summary

Given an integer array sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Return the number of unique elements `k`. The first `k` elements of the array must contain the unique numbers in sorted order.

## Brute Force Approach

Use an auxiliary list to store unique elements as we traverse the input array. Copy the unique elements back to the beginning of the original array.

```python
def removeDuplicates_bruteforce(nums):
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    for i in range(len(unique)):
        nums[i] = unique[i]
    return len(unique)
```

- Time Complexity: O(n^2) (due to list scanning `not in` membership check on each step, or O(n) if using a hash set with extra space)
- Space Complexity: O(n) for the auxiliary list/set.

## Optimized Approach

Since the array is already sorted, all duplicates are adjacent. We can use a two-pointer technique: a write pointer `k` initialized to 1 and a read pointer `i` traversing from 1 to the end. Whenever `nums[i]` is different from `nums[i-1]`, we write `nums[i]` to `nums[k]` and increment `k`.

```python
def removeDuplicates(nums):
    if not nums:
        return 0
    k = 1
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[k] = nums[i]
            k += 1
    return k
```

- Key idea: Use the sorted property to check adjacent elements and maintain a write boundary.
- Why it works: The read pointer scans through the elements, and by comparing the current element to the previous one, we identify new unique elements to copy to the front.

## Pattern Recognition

This is a classic Two Pointers (Read/Write) problem. One pointer acts as a writer/boundary for the final unique subarray, and the other pointer scans the elements.

## Key Observation

The sorted nature of the array means duplicate values will always be adjacent, making a simple comparison with the immediate predecessor sufficient to identify a unique element.

## Complexity Analysis

### Time Complexity

O(n) since the array is traversed exactly once.

### Space Complexity

O(1) because the duplicates are removed in-place without auxiliary data structures.

## Common Mistakes

- Not handling empty arrays correctly (returning 0 immediately).
- Comparing `nums[i]` to `nums[k-1]` or other elements instead of `nums[i-1]`.
- Creating a new list/array instead of modifying the existing one in-place.

## Interview Notes

This problem tests basic array manipulation skills, two-pointer boundary tracking, and in-place mutation. It is highly common in entry-level coding interviews.
