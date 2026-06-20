<h2><a href="https://leetcode.com/problems/3sum/">3Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Problem Summary

Given an integer array `nums`, return all unique triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`. The solution set must not contain duplicate triplets.

## Brute Force Approach

Use three nested loops to check all possible triplets. For each triplet, if their sum is 0, sort the triplet and insert it into a set to handle duplicates.

```python
def threeSum_bruteforce(nums):
    res = set()
    nums.sort()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    res.add((nums[i], nums[j], nums[k]))
    return [list(t) for t in res]
```

- Time Complexity: O(n^3) due to three nested loops.
- Space Complexity: O(k) where `k` is the number of unique triplets (needed for duplicate checking).

## Optimized Approach

Sort the array first. Iterate through the array with a pointer `i` from `0` to `len(nums) - 3`. If the current element is a duplicate of the previous element, skip it. For each fixed `nums[i]`, convert the problem to finding a pair in the remaining array that sums to `-nums[i]`. Use two pointers (`left = i + 1`, `right = len(nums) - 1`) to search inward. If the sum matches `-nums[i]`, store the triplet and adjust pointers, bypassing duplicates.

```python
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                s = nums[left] + nums[right]

                if s == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

                    while left < len(nums) and nums[left] == nums[left - 1]:
                        left += 1
                    while right >= 0 and nums[right] == nums[right + 1]:
                        right -= 1

                elif s < target:
                    left += 1
                else:
                    right -= 1

        return res
```

- Key idea: Use sorting to simplify duplicate detection and enable a two-pointer search on the remaining subarray.
- Why it works: For a fixed `nums[i]`, finding `nums[j] + nums[k] == -nums[i]` on a sorted subarray can be resolved in linear time by moving pointers based on whether the sum is less than or greater than the target.

## Pattern Recognition

This problem belongs to the Two Pointers pattern combined with sorting. Fixing one element and searching for the remaining pair on a sorted array is the standard extension of the Two Sum II pattern.

## Key Observation

The equation `nums[i] + nums[j] + nums[k] == 0` can be rewritten as `nums[j] + nums[k] == -nums[i]`. This transforms the problem into a Two Sum problem on a sorted array.

## Complexity Analysis

### Time Complexity

- Sorting the array takes O(n log n).
- The outer loop runs `n` times, and the inner two-pointer search runs in O(n) time for each iteration.
- Overall time complexity: O(n^2).

### Space Complexity

O(1) auxiliary space (excluding memory required for sorting).

## Common Mistakes

- Forgetting to sort the array.
- Skipping duplicate values only for the outer loop index `i` but forgetting to skip duplicates for the inner `left` and `right` pointers.
- Using a set to eliminate duplicate triplets, which adds unnecessary overhead.

## Interview Notes

Interviewers check if you can reduce the complexity from O(n^3) to O(n^2) and how cleanly you handle duplicate triplets without relying on a hash set.
