# 3Sum Closest

## Problem Summary

Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution.

## Brute Force Approach

Generate all possible triplets using three nested loops, calculate their sums, and keep track of the sum that has the minimum absolute difference from the target.

```python
def threeSumClosest_bruteforce(nums, target):
    min_diff = float('inf')
    res_sum = 0
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                total = nums[i] + nums[j] + nums[k]
                diff = abs(total - target)
                if diff < min_diff:
                    min_diff = diff
                    res_sum = total
    return res_sum
```

- Time Complexity: O(n^3) due to three nested loops.
- Space Complexity: O(1)

## Optimized Approach

Sort the array. Iterate through the array with a fixed index `i`. For each fixed element `nums[i]`, use two pointers (`left = i + 1`, `right = len(nums) - 1`) to find a pair such that the total sum of `nums[i] + nums[left] + nums[right]` is as close to the target as possible. Calculate the sum and update the result if the absolute difference `abs(total - target)` is smaller than the current minimum difference. Move pointers inward: if the sum is less than the target, increment `left`; if the sum is greater than the target, decrement `right`. If the sum equals the target, return the sum immediately.

```python
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        min_diff = float('inf')
        res_sum = 0

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                d = abs(total - target)

                if d < min_diff:
                    min_diff = d
                    res_sum = total

                if total == target:
                    return res_sum
                elif total < target:
                    left += 1
                else:
                    right -= 1

        return res_sum
```

- Key idea: Sort the array to enable logical inward pointer movement based on comparison with the target.
- Why it works: As the array is sorted, incrementing `left` increases the sum, and decrementing `right` decreases the sum, enabling us to search the closest value systematically.

## Pattern Recognition

This problem belongs to the Two Pointers pattern combined with sorting. Similar to 3Sum, we fix one element and use two pointers to find the closest pair in the remaining sorted subarray.

## Key Observation

Unlike the standard 3Sum, we do not need to collect all unique triplets or worry about skipping duplicate values to prevent duplicate triplets in the output. We only track the single best sum and its difference from the target.

## Complexity Analysis

### Time Complexity

- Sorting the array: O(n log n).
- Two-pointer traversal for each element: O(n^2).
- Overall time complexity: O(n^2).

### Space Complexity

O(1) auxiliary space.

## Common Mistakes

- Returning the absolute difference `abs(total - target)` instead of the sum `total`.
- Forgetting to update the closest sum when a smaller difference is found.
- Not terminating early when `total == target` is found.

## Interview Notes

This problem tests the capability to adapt the 3Sum two-pointer logic to optimization/difference tracking rather than finding exact matches.
