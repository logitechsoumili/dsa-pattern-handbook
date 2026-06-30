<h2><a href="https://leetcode.com/problems/move-zeroes/">Move Zeroes</a></h2> <img src='https://img.shields.io/badge/Difficulty-Easy-brightgreen' alt='Difficulty: Easy' />

## Problem Summary

Given an integer array `nums`, move all `0`s to the end of it while maintaining the relative order of the non-zero elements. You must do this in-place without making a copy of the array.

## Brute Force Approach

Create a new list. Iterate through the input array and copy all non-zero elements into the new array. Fill the remaining positions of the new array with zeros. Finally, copy all elements back to `nums`.

```python
def moveZeroes_bruteforce(nums):
    temp = []
    for num in nums:
        if num != 0:
            temp.append(num)
    while len(temp) < len(nums):
        temp.append(0)
    nums[:] = temp
```

- Time Complexity: O(n)
- Space Complexity: O(n) to store the auxiliary list.

## Optimized Approach

Use two pointers: a write pointer `curr` (initialized to 0) which tracks the position where the next non-zero element should be placed, and a read pointer `nxt` which scans the array from left to right. When a non-zero element is found at `nums[nxt]`, swap `nums[curr]` and `nums[nxt]`, and then increment `curr`.

- Key idea: Use swaps to push zeros backward and keep non-zero elements in their relative order.
- Why it works: At any point in the iteration, elements before `curr` are guaranteed to be non-zero in their correct relative order. Swapping ensures that non-zero elements move forward and zeros naturally float to the end.

## Python Solution (Reference)

```python
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        curr = 0  # position where next non-zero should be placed

        for nxt in range(len(nums)):
            if nums[nxt] != 0:
                nums[curr], nums[nxt] = nums[nxt], nums[curr]
                curr += 1
```

## C++ Solution (Primary)

```cpp
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int slow = 0;
        for (int fast = 0; fast < nums.size(); fast++){
            if (nums[fast] != 0){
                swap(nums[slow], nums[fast]);
                slow++;
            }
        }
    }
};
```

## Pattern Recognition

This problem belongs to the Two Pointers (Read/Write) pattern. It is very similar to Remove Duplicates or Partitioning algorithms, where one pointer scans the array (reader) and another pointer maintains the write boundary (writer).

## Key Observation

We do not need to track the position of zeros. By focusing only on placing non-zero elements sequentially at the write boundary `curr` using swaps, the zeros are automatically moved to the back.

## Complexity Analysis

### Time Complexity

O(n) because the array is traversed in a single pass with the read pointer `nxt`.

### Space Complexity

O(1) auxiliary space since the array elements are swapped in-place.

## Common Mistakes

- Using an extra array which violates the constant space constraint.
- Forgetting that the relative order of non-zero elements must remain unchanged.
- Maintaining two scanning pointers instead of a write pointer and a read pointer.

## Interview Notes

This problem evaluates array traversal, two-pointer write boundaries, and writing space-optimal solutions without auxiliary memory.
