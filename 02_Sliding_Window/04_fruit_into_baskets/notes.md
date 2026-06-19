# Fruit Into Baskets

## Problem Summary

You are given an integer array `fruits` where `fruits[i]` represents the type of fruit produced by the `i`-th tree. You have two baskets, and each basket can hold only one type of fruit. There is no limit on the amount of fruit each basket can hold. Starting from any tree, you must pick exactly one fruit from every tree while moving to the right. Return the maximum number of fruits you can collect.

## Brute Force Approach

Generate all possible subarrays. For each starting index, traverse to the right and insert fruit types into a set. Stop the traversal when the set size exceeds 2. Track the maximum subarray length.

```python
def totalFruit_bruteforce(fruits):
    max_fruits = 0
    for i in range(len(fruits)):
        basket = set()
        for j in range(i, len(fruits)):
            basket.add(fruits[j])
            if len(basket) > 2:
                break
            max_fruits = max(max_fruits, j - i + 1)
    return max_fruits
```

- Time Complexity: O(n^2) due to nested loops.
- Space Complexity: O(1) because the set stores at most 3 elements.

## Optimized Approach

This problem is equivalent to finding the longest contiguous subarray containing at most 2 distinct elements. Use a variable-size sliding window with a `left` pointer, `right` pointer, and a frequency map `basket`. Iterate `right` across the array and insert `fruits[right]` into `basket`. While `len(basket) > 2`, shrink the window by decrementing the count of `fruits[left]`, deleting the key if its count drops to 0, and incrementing `left`. At each step, update the maximum fruit count with `right - left + 1`.

```python
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        left = 0
        max_fruits = 0
        basket = {}

        for right in range(len(fruits)):
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            while len(basket) > 2:
                basket[fruits[left]] -= 1
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]
                left += 1

            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits
```

- Key idea: Map the problem description (picking 2 types of fruit from trees) to a mathematical constraint: finding the longest subarray with at most 2 distinct values.
- Why it works: Expanding the window adds elements, and when we violate the constraint of having at most 2 unique fruit types, we contract from the left to restore validity.

## Pattern Recognition

This problem belongs to the Variable-Size Sliding Window pattern. The objective is to maximize the window length subject to the constraint of containing at most 2 unique elements.

## Key Observation

The problem statement is heavily wrapped in a story (baskets, trees, picking fruits). Identifying that "baskets" are a constraint on the number of unique elements and that we need the "maximum number of fruits" (longest subarray) is the critical conversion step.

## Complexity Analysis

### Time Complexity

O(n) because each tree is visited at most twice (once by the `right` pointer and once by the `left` pointer).

### Space Complexity

O(1) auxiliary space because the `basket` frequency map will hold at most 3 keys at any time before shrinking.

## Common Mistakes

- Confusing the target metric: returning the number of unique fruit types (which is always at most 2) instead of the total number of fruits collected (the subarray length).
- Forgetting to delete the key from the map when the count of that fruit type drops to 0, which prevents the map size from decreasing.
- Using `if` instead of `while` to shrink the window, which fails when multiple elements need to be removed to make the window valid.
- Updating `max_fruits` before the window has been shrunk to a valid state.

## Interview Notes

This problem is a classic example of a "story-based" question that maps directly to a standard sliding window algorithm (Longest Subarray with at most K distinct elements, where K = 2). Interviewers use it to test a candidate's ability to translate business/real-world logic into algorithmic constraints.
