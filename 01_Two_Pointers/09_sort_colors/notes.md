<h2><a href="https://leetcode.com/problems/sort-colors/">Sort Colors</a></h2> <img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />

## Problem Summary

Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order 0 (Red), 1 (White), and 2 (Blue). Solve this without using the library sort function.

## Brute Force Approach

Create three separate arrays (buckets) to store 0s, 1s, and 2s. Traverse the input array, place each element into its corresponding bucket, and then overwrite `nums` with the concatenated buckets.

```python
def sortColors_bruteforce(nums):
    zeros = []
    ones = []
    twos = []

    for num in nums:
        if num == 0:
            zeros.append(num)
        elif num == 1:
            ones.append(num)
        else:
            twos.append(num)

    nums[:] = zeros + ones + twos
```

- Time Complexity: O(n)
- Space Complexity: O(n) because of the extra storage for buckets.

## Better Approach (Counting Sort)

Perform a first pass to count the frequencies of 0s, 1s, and 2s. Perform a second pass to overwrite the array with the correct number of 0s, 1s, and then 2s.

```python
def sortColors_counting(nums):
    count0 = count1 = count2 = 0

    for num in nums:
        if num == 0:
            count0 += 1
        elif num == 1:
            count1 += 1
        else:
            count2 += 1

    idx = 0
    for _ in range(count0):
        nums[idx] = 0
        idx += 1
    for _ in range(count1):
        nums[idx] = 1
        idx += 1
    for _ in range(count2):
        nums[idx] = 2
        idx += 1
```

- Time Complexity: O(n) (requires two passes)
- Space Complexity: O(1)

## Optimized Approach

Use the Dutch National Flag algorithm with three pointers: `low` (boundary of 0s), `mid` (current element), and `high` (boundary of 2s).
- If `nums[mid] == 0`: Swap `nums[low]` and `nums[mid]`, then increment both `low` and `mid`.
- If `nums[mid] == 1`: Increment `mid`.
- If `nums[mid] == 2`: Swap `nums[mid]` and `nums[high]`, then decrement `high`. Do *not* increment `mid` because the swapped element from `high` is unexplored and needs to be evaluated.

- Key idea: Maintain four dynamic subregions in a single pass using three pointers.
- Why it works: Swapping with `low` brings a known 0 or 1 to `mid`, so both can move forward. Swapping with `high` brings an unknown element to `mid`, requiring re-evaluation.

## Python Solution (Reference)

```python
class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else: # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
```

## C++ Solution (Primary)

```cpp
#include<bits/stdc++.h>
using namespace std;

class Solution {
public:
    void sortColors(vector<int>& nums) {
        int low = 0, mid = 0, high = nums.size() - 1;

        while (mid <= high){
            if (nums[mid] == 0){
                swap(nums[mid], nums[low]);
                low++;
                mid++;
            }
            else if (nums[mid] == 1) mid++;
            else{
                swap(nums[mid], nums[high]);
                high--;
            }
        }
    }
};
```

## Pattern Recognition

This problem is a classic three-way partitioning problem, which is a variation of the Two Pointers pattern. Instead of two regions, we maintain three sorted regions (0s, 1s, 2s) and an unexplored region in the middle.

## Key Observation

The array can be partitioned into:
- `[0, low)` containing only 0s.
- `[low, mid)` containing only 1s.
- `[mid, high]` representing the unexplored region.
- `(high, len(nums) - 1]` containing only 2s.

## Complexity Analysis

### Time Complexity

O(n) because each element is visited at most twice (and usually once), completed in a single pass.

### Space Complexity

O(1) auxiliary space as the partitioning is done in-place.

## Common Mistakes

- Incrementing `mid` after swapping with `high`. The swapped element from `high` is unexplored and could be `0` or `1`, so it must be processed in the next step.
- Using a library-based sort which takes O(n log n) time.
- Performing a two-pass counting sort when a single-pass solution is expected.

## Interview Notes

This is the standard Dutch National Flag problem created by Edsger Dijkstra. It evaluates a candidate's ability to maintain multiple pointers and subregion invariants simultaneously in a single pass.
