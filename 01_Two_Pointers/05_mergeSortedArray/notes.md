<h2><a href="https://leetcode.com/problems/merge-sorted-array/">Merge Sorted Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## Problem Summary

Given two sorted integer arrays `nums1` and `nums2`, merge them into a single sorted array in-place. The final sorted array should be stored inside `nums1`. `nums1` has a size of `m + n`, where the first `m` elements are the elements to be merged, and the last `n` elements are set to 0.

## Brute Force Approach

Concatenate `nums2` into `nums1` starting from index `m` and sort the entire `nums1` array.

```python
def merge_bruteforce(nums1, m, nums2, n):
    nums1[m:] = nums2
    nums1.sort()
```

- Time Complexity: O((m + n) log (m + n)) due to the sorting step.
- Space Complexity: O(1) or O(m + n) depending on the sorting algorithm.

## Optimized Approach

Start merging from the end of the arrays to avoid overwriting elements in `nums1`. Initialize three pointers: `i` at index `m - 1` (end of active elements in `nums1`), `j` at index `n - 1` (end of `nums2`), and `k` at index `m + n - 1` (end of `nums1` buffer). Compare elements at `i` and `j` and write the larger element to `k`, moving the corresponding pointers backward. If elements remain in `nums2` after pointer `i` falls below 0, copy them into the remaining positions of `nums1`.

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1
```

- Key idea: Work from right to left (largest to smallest) to leverage the empty buffer space at the end of `nums1`.
- Why it works: Writing to the end of `nums1` guarantees we never overwrite elements that we still need to process, since `k` is always greater than or equal to `i + n`.

## Pattern Recognition

This problem belongs to the Two Pointers pattern. Since we are merging two sorted structures, we use one pointer for each input array. Because we must merge in-place, we introduce a third pointer for writing to the target buffer.

## Key Observation

The empty buffer at the end of `nums1` allows us to merge without allocating auxiliary memory if we place elements starting from the largest value (end of array) rather than the smallest (start of array).

## Complexity Analysis

### Time Complexity

O(m + n) because we process each of the `m + n` elements exactly once.

### Space Complexity

O(1) auxiliary space as the merge operation is done entirely in-place in `nums1`.

## Common Mistakes

- Merging from the front, which overwrites values in `nums1` before they are processed.
- Forgetting to copy remaining elements from `nums2` when `nums1` is exhausted (`i < 0`).
- Trying to copy remaining elements from `nums1` when `nums2` is exhausted (they are already in their correct places).

## Interview Notes

This problem evaluates a candidate's understanding of array layouts and how to optimize in-place merges by changing the direction of traversal (backwards instead of forwards).
