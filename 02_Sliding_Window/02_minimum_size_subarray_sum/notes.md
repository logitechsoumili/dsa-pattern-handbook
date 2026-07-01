<h2><a href="https://leetcode.com/problems/minimum-size-subarray-sum/">Minimum Size Subarray Sum</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Problem Summary

Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a contiguous subarray whose sum is greater than or equal to `target`. If there is no such subarray, return `0`.

## Brute Force Approach

Generate all possible contiguous subarrays. For each starting index, extend the subarray until the sum becomes greater than or equal to `target`, then record the length. Track the overall minimum length.

```python
def minSubArrayLen_bruteforce(target, nums):
    min_len = float('inf')
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum += nums[j]
            if curr_sum >= target:
                min_len = min(min_len, j - i + 1)
                break
    return 0 if min_len == float('inf') else min_len
```

```cpp
int minSubArrayLen_bruteforce(int target, vector<int>& nums) {
    int minLen = INT_MAX;
    for (int i = 0; i < nums.size(); i++) {
        int currSum = 0;
        for (int j = i; j < nums.size(); j++) {
            currSum += nums[j];
            if (currSum >= target) {
                minLen = min(minLen, j - i + 1);
                break;
            }
        }
    }
    return minLen == INT_MAX ? 0 : minLen;
}
```

- Time Complexity: O(n^2) due to nested loops.
- Space Complexity: O(1)

## Optimized Approach

Use a variable-size sliding window. Maintain a `left` pointer and a running `window_sum`. Expand the window by iterating a `right` pointer across the array. For each element added, check if `window_sum >= target`. While this condition is met, update the minimum length with `right - left + 1`, subtract `nums[left]` from `window_sum`, and increment `left` to shrink the window and find smaller valid subarrays.

```python
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_len = float('inf')
        left = 0
        window_sum = 0

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                min_len = min(min_len, right - left + 1)
                window_sum -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
```

```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int left = 0, currentSum = 0;
        int minLen = INT_MAX;

        for (int right = 0; right < nums.size(); right++){
            currentSum += nums[right];

            while (currentSum >= target){
                minLen = min(minLen, right - left + 1);
                currentSum -= nums[left];
                left++;
            }
        }
        return minLen == INT_MAX ? 0 : minLen;
    }
};
```

- Key idea: Dynamically adjust the window size based on the validity of the current subarray sum.
- Why it works: Since all elements are positive, adding elements increases the sum (expands window) and removing elements decreases the sum (shrinks window). This allows us to skip redundant checks.

## Pattern Recognition

This problem belongs to the Variable-Size Sliding Window pattern. The objective is to find the minimum length of a contiguous subarray that satisfies a threshold condition (sum >= target).

## Key Observation

Once we find a valid window, any further expansion of that window from the right will only increase its length and sum. Therefore, we should immediately attempt to shrink it from the left to search for a smaller valid length.

## Complexity Analysis

### Time Complexity

O(n) because each element is visited at most twice: once when the `right` pointer expands the window and once when the `left` pointer shrinks it.

### Space Complexity

O(1) auxiliary space.

## Common Mistakes

- Applying a fixed-size sliding window template when the window size needs to be variable.
- Forgetting to shrink the window from the left once the sum meets the target, which leaves the solution at O(n^2) if handled incorrectly.
- Updating `min_len` after shrinking the pointer instead of before.
- Returning `float('inf')` instead of `0` when no valid subarray is found.

## Interview Notes

This problem tests the ability to implement a variable-size sliding window with a dynamic shrinking phase. It is an excellent test of pointer manipulation and boundary conditions.
