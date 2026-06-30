<h2><a href="https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/">Two Sum II - Input Array Is Sorted</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Problem Summary

Given a 1-indexed array of integers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the 1-based indices of the two numbers. The solution must use constant extra space.

## Brute Force Approach

Iterate through every pair of elements using nested loops and check if their sum equals the target.

```python
def brute_force(arr, target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return (i, j)
    return None
```

- Time Complexity: O(n^2)
- Space Complexity: O(1)

## Better Approach (Hash Map)

Use a hash map to store the elements and their corresponding indices. While iterating, check if the complement (`target - val`) exists in the map.

```python
def better(arr, target):
    index_map = {}
    for i, val in enumerate(arr):
        comp = target - val
        if comp in index_map:
            return index_map[comp], i
        index_map[val] = i
    return None
```

- Time Complexity: O(n)
- Space Complexity: O(n)

## Optimized Approach

Use a two-pointer technique with one pointer at the start and one at the end of the array. Sum the elements at both pointers. If the sum is equal to the target, return the indices. If the sum is less than the target, move the left pointer rightward to increase the sum. If the sum is greater than the target, move the right pointer leftward to decrease the sum.

- Key idea: Leverage the sorted nature of the array to eliminate search space dynamically.
- Why it works: Since the array is sorted, incrementing the left pointer guarantees a sum that is greater than or equal to the previous sum, and decrementing the right pointer guarantees a sum that is less than or equal to the previous sum.

## Python Solution (Reference)

```python
def optimised(arr, target):
    i, j = 0, len(arr) - 1
    while i < j:
        res = arr[i] + arr[j]
        if res == target:
            return (i, j)
        elif res < target:
            i += 1
        else:
            j -= 1
    return None
```

## C++ Solution (Primary)

```cpp
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int left = 0, right = numbers.size() - 1;

        while (left < right){
            int res = numbers[left] + numbers[right];
            if (res == target){
                return {left+1, right+1};
            }
            else if (res < target){
                left++;
            }
            else{
                right--;
            }
        }
        return {0,0};
    }
};
```

## Pattern Recognition

This problem belongs to the Two Pointers pattern because the input array is sorted and we are searching for a pair that meets a specific condition (sum equals target). Starting pointers at both ends and moving them inward allows us to process the array in a single pass.

## Key Observation

The sorted order of the array allows us to make binary decisions at each step: if the current sum is too small, we must increment the left pointer; if it is too large, we must decrement the right pointer.

## Complexity Analysis

### Time Complexity

O(n) because each element is visited at most once by either pointer.

### Space Complexity

O(1) as only a constant amount of extra memory is used for the two pointers.

## Common Mistakes

- Forgetting that the problem asks for 1-indexed results (though standard binary search or two pointers might return 0-based indices).
- Not checking for empty arrays or arrays with fewer than two elements.
- Incrementing the left pointer when the sum is greater than the target.

## Interview Notes

Interviewers test the ability to optimize an O(n^2) brute force or O(n) space hashmap solution to O(1) space by exploiting the sorted property of the input array.
