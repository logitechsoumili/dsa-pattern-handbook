<h2><a href="https://www.geeksforgeeks.org/problems/segregate-0s-and-1s5106/1">Segregate 0s and 1s</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## Problem Summary

Given an array consisting of only 0s and 1s in random order, modify the array in-place to segregate all 0s onto the left side and all 1s onto the right side.

## Brute Force Approach

Count the number of 0s in the array. Overwrite the first `count` elements with 0 and the remaining elements with 1.

```python
def segregate0and1_counting(arr):
    count0 = arr.count(0)
    for i in range(count0):
        arr[i] = 0
    for i in range(count0, len(arr)):
        arr[i] = 1
    return arr
```

- Time Complexity: O(n) (requires two passes: one for counting, one for overwriting)
- Space Complexity: O(1)

## Optimized Approach

Use a two-pointer style partition algorithm. Maintain a pointer `k` representing the boundary of where the next 0 should be placed. Traverse the array with a pointer `i`. If `arr[i]` is 0, swap `arr[k]` and `arr[i]`, then increment `k`.

```python
def segregate0and1(arr):
    k = 0
    for i in range(len(arr)):
        if arr[i] == 0:
            arr[k], arr[i] = arr[i], arr[k]
            k += 1
    return arr
```

- Key idea: Use a write pointer to dynamically build the 0-region as we traverse.
- Why it works: Every time we encounter a 0, swapping it with the element at the boundary pointer `k` ensures that all elements before `k` are 0, and the scanned 1s get pushed to the right.

## Pattern Recognition

This problem is a basic partitioning pattern, which is a common variation of Two Pointers. One pointer acts as a writer (tracking the boundary of sorted 0s) while the other acts as a reader scanning the elements.

## Key Observation

By using in-place swaps when finding a 0, we can achieve segregation in a single pass without storing frequency counts or using extra memory.

## Complexity Analysis

### Time Complexity

O(n) since the array is traversed exactly once.

### Space Complexity

O(1) because the partitioning and swapping are performed in-place.

## Common Mistakes

- Modifying the array but not in-place (e.g. creating new arrays).
- Off-by-one errors with the partition boundary pointer.
- Two-pass counting when a single-pass solution is requested.

## Interview Notes

This is a fundamental partition problem similar to the QuickSort partition step and the Dutch National Flag problem. It tests the candidate's ability to mutate arrays in-place with minimal passes.
