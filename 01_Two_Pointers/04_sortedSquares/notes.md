<h2><a href="https://leetcode.com/problems/squares-of-a-sorted-array/">Squares of a Sorted Array</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## Problem Summary

Given an integer array sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

## Brute Force Approach

Square every element in the input array, and then sort the resulting array.

```python
def sortedSquares_bruteforce(arr):
    new = [x**2 for x in arr]
    new.sort()
    return new
```

- Time Complexity: O(n log n) due to the sorting step.
- Space Complexity: O(n) to store the squared array.

## Alternate Merge Approach

Find the split point between negative and non-negative numbers. Square both parts separately and merge them.

```python
def sortedSquares_merge(arr):
    if not arr:
        return []

    neg, pos = [], []

    for i in range(len(arr)-1):
        if arr[i] < 0 and arr[i+1] >= 0:
            neg = [x**2 for x in arr[:i+1]][::-1]
            pos = [x**2 for x in arr[i+1:]]
            break

    if not neg and not pos:
        if arr[0] >= 0:
            pos = [x**2 for x in arr]
            return pos
        else:
            neg = [x**2 for x in arr]
            return neg[::-1]

    res = []
    i, j = 0, 0

    while (i < len(neg) and j < len(pos)):
        if neg[i] <= pos[j]:
            res.append(neg[i])
            i += 1
        else:
            res.append(pos[j])
            j += 1

    while (i < len(neg)):
        res.append(neg[i])
        i += 1

    while (j < len(pos)):
        res.append(pos[j])
        j += 1

    return res
```

- Time Complexity: O(n)
- Space Complexity: O(n) (requires intermediate arrays for storing negative and positive parts)

## Optimized Approach

Use a two-pointer approach starting from the ends of the array. Compare the absolute values or squares of the elements at the left and right pointers. Append the larger square to the result, and move the corresponding pointer inward. Since the largest squares are processed first, reverse the final result to obtain non-decreasing order.

- Key idea: The largest squared values in a sorted array containing negative numbers will always reside at either the extreme left (large negative values) or extreme right (large positive values).
- Why it works: Comparing the ends allows us to identify the largest squared values sequentially in O(n) time without sorting.

## Python Solution (Reference)

```python
def sortedSquares_twoPointer(arr):
    res = []
    i, j = 0, len(arr) - 1

    while i <= j:
        if arr[i]**2 >= arr[j]**2:
            res.append(arr[i]**2)
            i += 1
        else:
            res.append(arr[j]**2)
            j -= 1
    return res[::-1]
```

## C++ Solution (Primary)

```cpp
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> res(nums.size());
        int pos = nums.size() - 1;
        int left = 0, right = nums.size() - 1;

        while (left <= right){
            int a = nums[left] * nums[left];
            int b = nums[right] * nums[right];

            if (a > b){
                res[pos--] = a;
                left++;
            }
            else{
                res[pos--] = b;
                right--;
            }
        }

        return res;
    }
};
```

## Pattern Recognition

This problem belongs to the Two Pointers pattern. The input array is sorted and contains both negative and positive numbers. Since the squaring operation maps large negative values to large positive values, the largest squared values are at the boundaries, suggesting a two-pointer approach starting from both ends.

## Key Observation

The squared values of a sorted array containing negative numbers are ordered like a V-shape: descending for negative numbers and ascending for positive numbers. The maximum value is always at one of the two ends.

## Complexity Analysis

### Time Complexity

O(n) because each element is processed exactly once by the two pointers.

### Space Complexity

O(n) for the output array. No other extra arrays are created.

## Common Mistakes

- Forgetting to reverse the result array if appending from largest to smallest.
- Ignoring negative numbers and just squaring elements in-place without sorting.
- Not taking advantage of the sorted property, resulting in an O(n log n) sorting solution.

## Interview Notes

This problem evaluates how well candidates can exploit sorted arrays containing negative numbers to construct an O(n) linear-time solution instead of sorting.
