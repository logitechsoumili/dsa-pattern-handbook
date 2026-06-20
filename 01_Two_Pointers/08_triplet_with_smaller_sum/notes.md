<h2><a href="https://www.geeksforgeeks.org/problems/count-triplets-with-sum-smaller-than-x5549/1">Triplets with Smaller Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Problem Summary

Given an array of distinct integers and a target value `sum`, find the count of triplets `(i, j, k)` with `i < j < k` such that `arr[i] + arr[j] + arr[k] < sum`.

## Brute Force Approach

Use three nested loops to examine all triplets, compute their sums, and increment a counter if the sum is less than the target.

```python
def countTriplets_bruteforce(arr, sum_val):
    ans = 0
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] < sum_val:
                    ans += 1
    return ans
```

- Time Complexity: O(n^3) due to three nested loops.
- Space Complexity: O(1)

## Optimized Approach

Sort the array first. Iterate through the array, fixing the first element `arr[i]`. Use two pointers (`left = i + 1`, `right = len(arr) - 1`) to find pairs. If `arr[i] + arr[left] + arr[right] < sum`, then because the array is sorted, any element at index `k` where `left < k <= right` will also form a valid triplet with `arr[i]` and `arr[left]`. Thus, we can count all `right - left` valid triplets at once and increment `left` to search for larger values. If the sum is greater than or equal to `sum`, decrement `right` to reduce the sum.

```python
class Solution:
    def countTriplets(self, sum, arr):
        arr.sort()
        ans = 0

        for i in range(len(arr) - 2):
            left = i + 1
            right = len(arr) - 1

            while left < right:
                total = arr[i] + arr[left] + arr[right]

                if total >= sum:
                    right -= 1
                else:
                    ans = ans + (right - left)
                    left += 1

        return ans
```

- Key idea: Use the sorted property of the array to count multiple valid triplets in constant time.
- Why it works: For a fixed `arr[i]` and `arr[left]`, if the largest possible third element `arr[right]` yields a sum less than target, all elements between `left` and `right` are guaranteed to yield sums less than target because they are smaller than or equal to `arr[right]`.

## Pattern Recognition

This problem belongs to the Two Pointers pattern combined with sorting. It is a variation of the 3Sum problem where instead of finding an exact match or closest sum, we count combinations satisfying an inequality.

## Key Observation

The crucial step in the two-pointer loop is:
`ans += (right - left)`
This allows counting all valid triplets for a fixed pair `(arr[i], arr[left])` in O(1) time instead of iterating through them.

## Complexity Analysis

### Time Complexity

- Sorting the array: O(n log n).
- Two-pointer traversal for each outer element: O(n^2).
- Overall time complexity: O(n^2).

### Space Complexity

O(1) auxiliary space.

## Common Mistakes

- Incrementing the answer by 1 (`ans += 1`) instead of `ans += (right - left)`.
- Forgetting to sort the array.
- Moving the `left` pointer when the sum is too large.
- Attempting to store all triplets in memory when only the count is requested.

## Interview Notes

Interviewers test the candidate's understanding of how sorted arrays allow counting groups of solutions in O(1) step time rather than enumerating them.
